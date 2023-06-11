setup: requirements.txt
	pip install -r requirements.txt

format:
	isort .
	autopep8 --in-place *.py
	flake8 .
