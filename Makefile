freeze:
		@echo "Freezing current environment's packages to requirements.txt"
		pip freeze > requirements.txt
		@echo "requirements.txt has been updated."

clean:
		@echo "Removing requirements.txt"
		rm -f requirements.txt
		@echo "requirements.txt has been removed."

install:
		@echo "Installing packages from requirements.txt"
		pip install -r requirements.txt
		@echo "Packages have been installed."
