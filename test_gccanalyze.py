try:
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO

try:
    # Python 2.6
    import unittest2 as unittest
except:
    import unittest

import gccanalyze


class TestUnits(unittest.TestCase):

    def test_split_warnings(self):
        self.assertEqual(
            ["bad.cc: In function 'int main()':\nbad.cc:5:19: warning: declaration of 'foo' shadows a previous local [-Wshadow]",
             "bad.cc:3:15: warning: shadowed declaration is here [-Wshadow]",
             "bad.cc:5:19: warning: unused variable 'foo' [-Wunused-variable]"],
            list(gccanalyze.split_warnings(
            """
bad.cc: In function 'int main()':
bad.cc:5:19: warning: declaration of 'foo' shadows a previous local [-Wshadow]
bad.cc:3:15: warning: shadowed declaration is here [-Wshadow]
bad.cc:5:19: warning: unused variable 'foo' [-Wunused-variable]
""")))


class TestSystem(unittest.TestCase):

    def check(self, expected_warnings, arguments):
        output_file = StringIO()
        gccanalyze.main(argv=['gccanalyze'] + arguments,
                        standard_out=output_file)
        if expected_warnings is None:
            self.assertFalse(output_file.getvalue().strip())
        else:
            self.assertEqual(
                sorted(expected_warnings),
                sorted(extract_warnings(output_file.getvalue())))

    def test_okay(self):
        self.check(None, ['okay.cc'])

    def test_okay_with_strict_shadow(self):
        self.check(['shadow', 'shadow'],
                   ['--strict-shadow', 'okay.cc'])

    def test_bad(self):
        self.check(['shadow', 'shadow', 'unused-variable'],
                   ['bad.cc'])


def extract_warnings(message):
    """Return list of warning categories."""
    for line in message.split('\n'):
        line = line.strip()
        if '[-W' in line and line.endswith(']'):
            warning = line.rsplit('[', 1)[1]
            if warning.startswith('-W'):
                assert warning.endswith(']')
                yield warning[2:-1]


if __name__ == '__main__':
    unittest.main()
