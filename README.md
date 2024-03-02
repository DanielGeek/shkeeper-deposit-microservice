# shkeeper-deposit-microservice
Microservices in Python integrated with SHKeeper API for managing cripto deposit flows 

# Folder structure
- app/: Contains your Flask application and its components.
- __init__.py: Initializes your Flask application and brings together other components.
- models.py: Defines data models, if you're interacting with a database.
- routes.py: Contains all the route definitions for your application.
- utils.py: Helper functions and utilities.
- tests/: Contains your unit and integration tests.
- requirements.txt: Lists all the Python packages your project depends on.
- config.py: Configuration settings for your application, like API keys and environment-specific settings.
- .env: Stores environment variables (make sure this is added to .gitignore to keep secrets out of version control).
- run.py: The entry point to run your Flask application.