INTERP=python
MANAGE_FILE=manage.py
REQ_FILE=requirements.txt
INSTALLER=pip install -r

SHELL=/bin/bash

run:
	@$(INTERP) $(MANAGE_FILE) runserver > /dev/null 2> /dev/null &


stop:
	@kill `ps -ef | grep python | grep runserver | grep -v grep | awk '{print $$2}'`


install:
	$(INSTALLER) $(REQ_FILE)


