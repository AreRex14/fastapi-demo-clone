# fastapi-demo-clone
from https://docs.wayscript.com/quickstart/set-up-fastapi-server

## Dependencies

The requirements include:
* fastAPI
* uvicorn

Found in Requirements.txt

## Setup

Trigger Configuration:
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8080


App specific code:
Each route can be found within main.py .
To define the type of request you expect from the user, you denote it using the method of the corresponding method on @app.
The function underneath each decorated @app defines the logic for that url endpoint
