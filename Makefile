install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=main tests/test_*.py

format:
	black . *.py

lint:
	pylint --disable=R,C *.py 

all: install lint test format
