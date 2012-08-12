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

    def check(self, expected, arguments):
        output_file = StringIO()
        gccanalyze.main(argv=['gccanalyze'] + arguments,
                        standard_out=output_file)
        self.assertEqual(
            expected.strip(),
            output_file.getvalue().strip())

    def test_okay(self):
        self.check('', ['okay.cc'])

    def test_okay_with_strict_shadow(self):
        self.check("""
okay.cc: In member function 'int Foo::bar()':
okay.cc:10:19: warning: declaration of 'foo' shadows a member of 'this' [-Wshadow]
""", ['--strict-shadow', 'okay.cc'])

    def test_bad(self):
        self.check("""
bad.cc: In function 'int main()':
bad.cc:5:19: warning: declaration of 'foo' shadows a previous local [-Wshadow]
bad.cc:3:15: warning: shadowed declaration is here [-Wshadow]
bad.cc:5:19: warning: unused variable 'foo' [-Wunused-variable]
""", ['bad.cc'])


if __name__ == '__main__':
    unittest.main()
