==========
gccanalyze
==========

Do static analysis with GCC.

.. image:: https://secure.travis-ci.org/myint/gccanalyze.png
   :target: https://secure.travis-ci.org/myint/gccanalyze
   :alt: Build status


-------
Example
-------

Only interesting shadowing cases are shown::

    $ gccanalyze bad.cc

    bad.cc: In function 'int main()':
    bad.cc:5:19: warning: declaration of 'foo' shadows a previous local [-Wshadow]
    bad.cc:3:15: warning: shadowed declaration is here [-Wshadow]
    bad.cc:5:19: warning: unused variable 'foo' [-Wunused-variable]
