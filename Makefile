check:
	@pep8 gccanalyze gccanalyze.py setup.py
	@echo .
	@pep257.py gccanalyze gccanalyze.py setup.py
	@echo .
	@pylint --report=no --include-ids=yes --disable=F0401,R0914,E1103,E1120 --rcfile=/dev/null gccanalyze.py setup.py
	@echo .
	@python setup.py --long-description | rst2html --strict > /dev/null
	@scspell gccanalyze gccanalyze.py setup.py test_gccanalyze.py README.rst

coverage:
	@rm -f .coverage
	@coverage run test_gccanalyze.py
	@coverage report
	@coverage html
	@rm -f .coverage
	@python -m webbrowser -n "file://${PWD}/htmlcov/index.html"

mutant:
	@mut.py -t gccanalyze -u test_gccanalyze -mc

readme:
	@python setup.py --long-description | rst2html --strict > README.html
	@python -m webbrowser -n "file://${PWD}/README.html"

register:
	@python setup.py register
	@python setup.py sdist upload
	@srm ~/.pypirc
