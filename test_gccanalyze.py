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


class TestSystem(unittest.TestCase):

    def check(self, expected_warnings, arguments):
        output_file = StringIO()
        gccanalyze.main(argv=['gccanalyze'] + arguments,
                        standard_out=output_file)
        self.assertEqual(
            sorted(expected_warnings),
            sorted(extract_warnings(output_file.getvalue())))

    def test_okay(self):
        self.check('', ['okay.cc'])

    def test_okay_with_strict_shadow(self):
        self.check(['shadow'],
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
