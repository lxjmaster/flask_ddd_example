PROJECT_NAME=$(shell pwd)

lint:
	command python3.11 -m pip install --upgrade pip && pip3.11 install pylint
	pylint --disable=missing-module-docstring $(PROJECT_NAME)