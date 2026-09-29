from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

contacts = []


class Contact(BaseModel):
    name: str
    phone: str
    email: str



@app.get("/")
def home():
    return {
        "message": "Welcome to Contact API!"
    }



@app.post("/addcontact")
def add_contact(contact: Contact):
    contacts.append(contact)

    return {
        "message": "Contact added successfully",
        "name": contact.name
    }



@app.get("/getcontacts")
def get_contacts():
    return {
        "contacts": contacts
    }