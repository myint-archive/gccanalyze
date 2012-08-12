#!/usr/bin/env python
"""Setup for gccanalyze."""

from distutils import core


def version():
    """Return version string."""
    with open('gccanalyze') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                import ast
                return ast.literal_eval(line.split('=')[1].strip())


with open('README.rst') as readme:
    core.setup(name='gccanalyze',
               version=version(),
               description='Do static analysis with GCC.',
               long_description=readme.read(),
               license='Expat License',
               author='myint',
               url='https://github.com/myint/gccanalyze',
               classifiers=['Intended Audience :: Developers',
                            'Environment :: Console',
                            'Programming Language :: Python :: 2.6',
                            'Programming Language :: Python :: 2.7',
                            'Programming Language :: Python :: 3',
                            'License :: OSI Approved :: MIT License'],
               scripts=['gccanalyze'])
