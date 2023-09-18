#!/usr/bin/python3
"""
Defines a User class that extends BaseModel.
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Class to represent a user"""
    first_name = ""
    surname = ""
    email = ""
    password = ""
        
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def authenticate(self, password):
        return self.password == password
