from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    description : Union[str, None] = None
    price : float
    tax : Union[float, None] = None

# Creates our FastAPI application
app = FastAPI()

# Home route
# returns JSON response of dictionary after the return statement
@app.get("/")
def home():
    return {'data': 'Hello world'}

# Route allowing variable URL
# Function uses what the value of what is passed in the {item} position as a variable
# in this example we just return whatever the user sends as {item} in the URL back to the user as a JSON response
@app.get("/search/{item}")
def search(item: str):
    return {'data' : item}

# POST Endpoint
# We expect the user's POST body to contain all parameters of our Item class (Defined Above)
# The parameters' types must match our class variable types or an error is returned to the user.
@app.post("/items/")
def create_item(item : Item):
    return item
