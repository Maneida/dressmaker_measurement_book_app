#!/usr/bin/python3
"""
Contains the Template class
"""
import models
from models.base_model import BaseModel

class Template(BaseModel):
    def __init__(self, user_id, name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.name = name if name else self._generate_custom_name(user_id)
        self.measurements = []

    def _generate_custom_name(self, user_id, number=1):
        name = "Custom Template ({})".format(number)
        user = models.storage.get(User, user_id)

        if user:
            user_templates = user.templates_list
            matching_templates = [template for template in user_templates if template.name == name]

            if matching_templates:
                return self._generate_custom_name(user_id, number + 1)

        return name

    def add_measurement(self, measurement):
        self.measurements.append(measurement)

    def remove_measurement(self, measurement):
        if measurement in self.measurements:
            self.measurements.remove(measurement)
        else:
            print(f"{measurement} not found in the template.")

    def edit_measurement(self, old_measurement, new_measurement):
        try:
            index = self.measurements.index(old_measurement)
            self.measurements[index] = new_measurement
        except ValueError as e:
            print(f"Error editing measurement: {e}")
