#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
import models
from models.base_model import BaseModel
from models.customer import Customer
from models.user import User

classes = {"BaseModel": BaseModel, "Customer": Customer, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
            # with open(self.__file_path, 'w') as f:
            #     json.dump({}, f)
        except Exception as e:
            print("Error: {}".format(e))

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """ Gets and object through its class and id, passed as
            arguments
        """
        if cls in classes.values() and id:
            key = '{}.{}'.format(cls.__name__, id)
            objs = self.all(cls)
            return objs.get(key)
        return None

    def count(self, cls=None):
        """ Returns count of objects in a class passed as argument
        """
        all_cls_objs = self.all(cls)
        return len(all_cls_objs)
