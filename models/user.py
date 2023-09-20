#!/usr/bin/python3
"""
Defines a User class that extends BaseModel.
"""
import models
from models.base_model import BaseModel
from models.template import Template



class User(BaseModel):
    """Class to represent a user"""
    first_name = ""
    surname = ""
    email = ""
    password = ""
    templates_list = []
        
    def __init__(self, *args, **kwargs):
        """
        Initializes user.

        If `templates_list` is empty, creates a default template.
        """
        super().__init__(*args, **kwargs)

        if not self.templates_list:
            self._create_default_template()

    def _create_default_template(self):
        """Create a default template for the user."""
        default_measurements = {
            'Hip': 0,
            'Waist': 0,
            'Sleeve length': 0
        }

        default_template = Template(user_id=self.id, name="default", measurements=default_measurements)
        default_template.save()
        self.templates_list.append(default_template.id)


    def authenticate(self, password):
        """Authenticate user based on provided password."""
        return self.password == password

    def add_template(self, template_id):
        """
        Add a template to the user's templates list.

        Args:
            template_id (str): ID of the template to add.
        """
        # might not be necessary
        self.templates_list.append(template_id)
