# Name of the virtual environment
VENV = .venv

# Path to the Python interpreter in the virtual environment
PYTHON = $(VENV)/bin/python

# Path to pip in the virtual environment
PIP = $(VENV)/bin/pip

# Name of the main module of the project
MODULE = fastapi_project.main:app

# Default command to install dependencies
install:
	@echo "Installing Python packages..."
	@$(PIP) install -r requirements.txt

# Command to create a virtual environment
venv:
	@echo "Creating virtual environment..."
	@python3 -m venv $(VENV)
	@$(MAKE) install

# Command to run the application
run:
	@echo "Running the application..."
	@$(PYTHON) -m uvicorn $(MODULE) --reload

# Command to format the code
format:
	@echo "Formatting code..."
	@$(PYTHON) -m black .

# Command for linting the code
lint:
	@echo "Linting code..."
	@$(PYTHON) -m flake8 .

# Command for tests
test:
	@echo "Running tests..."
	@$(PYTHON) -m pytest

# Command to clean the environment
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV)
	@find . -type d -name "__pycache__" -exec rm -r {} +

# Command to build Docker
docker-build:
	@echo "Building Docker images..."
	@docker-compose build

# Command to run Docker
docker-up:
	@echo "Starting Docker containers..."
	@docker-compose up -d

# Command to stop Docker
docker-down:
	@echo "Stopping Docker containers..."
	@docker-compose down

# Command to clean Docker environment
docker-clean:
	@echo "Removing Docker containers, networks, and images..."
	@docker-compose down --volumes --rmi all

# Default command
default: venv

.PHONY: install venv run format lint test clean docker-build docker-up docker-down docker-clean default
