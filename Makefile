WORKDIR = yatube_api
TEMPLATES-DIR = $(WORKDIR)/templates
MANAGE = python $(WORKDIR)/manage.py

style:
	black -S -l 79 $(WORKDIR)
	isort $(WORKDIR)
	flake8 $(WORKDIR)
	mypy $(WORKDIR)