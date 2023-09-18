import models
from models.base_model import BaseModel
from models.user import User

class Customer(BaseModel):
    address = ""
    email = ""
    
    
    def __init__(self, user_id, *args, **kwargs):
        """
        Initialize a Customer instance.

        Args:
            user_id (str): The ID of the associated User.
        """
        # Check if the user with the provided user_id exists
        user = models.storage.get(User, user_id)

        if not user:
            raise ValueError(f"User with ID {user_id} does not exist.")
        
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.first_name = ""
        self.surname = ""
        self.phone_number = ""
        self.measurements = {}
        default_list = ['Bust', 'Waist', 'Hip', 'Shoulder to Nipple',
                        'Shoulder to Waist', 'Shoulder to Hip',
                        'Nipple to Nipple', 'Sleeve Length', 'Around Arm',
                        'Across Back']

        for i in default_list:
            self.measurements[i] = None

    def get_measurement(self, key):
        return self.measurements.get(key)

    def set_measurement(self, key, value):
        self.measurements[key] = value
