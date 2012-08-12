try:
    # Python 2.6
    import unittest2 as unittest
except:
    import unittest

import subprocess


class TestSystem(unittest.TestCase):

    def check(self, expected, arguments):
        process = subprocess.Popen(['./gccanalyze'] + arguments,
                                   stdout=subprocess.PIPE)
        (output, _) = process.communicate()
        self.assertEqual(expected.strip(), output.decode('utf-8').strip())

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
