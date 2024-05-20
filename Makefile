.PHONY: install run

install:
		pip install -r requirements.txt
		python -m pip install --upgrade pip
		echo "-dependencies installed"


run:
	        python manage.py runserver
