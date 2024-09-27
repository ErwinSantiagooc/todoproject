# Variables
PYTHON=python
MANAGE=manage.py
RUFF=ruff

# Virtual environment
VENV_DIR=venv

# activate Virtual environment
activate:
	$(VENV_DIR)\Scripts\activate

# Install dependencies
install:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)\Scripts\pip install -r requirements.txt

# Migrate the database
migrate:
	$(PYTHON) $(MANAGE) migrate

# Create migrations
makemigrations:
	$(PYTHON) $(MANAGE) makemigrations

# Running the development server
runserver:
	$(PYTHON) $(MANAGE) runserver

# Create superuser
createsuperuser:
	$(PYTHON) $(MANAGE) createsuperuser

# Clear Python temporary and cache files
clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "*.pyo" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

# Execute tests
test:
	$(PYTHON) $(MANAGE) test

# Deploy the project in production
deploy:
	$(PYTHON) $(MANAGE) collectstatic --noinput
	$(PYTHON) $(MANAGE) migrate

# Targets
.PHONY: run test lint

# ruff
test:
	$(PYTHON) -m unittest discover

lint:
	$(RUFF) .