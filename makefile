#makefile

install:
		pip install --upgrade pip 

format:
		black *.py

lint:
		pylint --disable=R,C script.py

test:
		python3 -m pytest test_*.py

all: install format lint test