#!/usr/bin/python3
"""
MBook console
"""
import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.customer import Customer
from models.template import Template
from models.user import User
import shlex
import argparse

classes = {"BaseModel": BaseModel, "Customer": Customer, "User": User,
           "Template": Template}

class MBookCommand(cmd.Cmd):
    """MBook console class"""
    prompt = '(MBook) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_exit(self, arg):
        """Command to exit programme"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        try:
            if len(args) == 0:
                print("** class name missing **")
                return False
            if args[0] in classes:
                new_dict = self._key_value_parser(args[1:])
                instance = classes[args[0]](**new_dict)
            else:
                print("** class doesn't exist **")
                return False
            print(instance.id)
            instance.save()
        except Exception as e:
            print(f"An error occurred: {e}")

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """
        Update an instance based on the class name, id, attribute & value.

        Usage:
            do_update class_name instance_id attribute value

        Example:
            update Customer a536b743-416f-46a6-97e7-9261550dc94a name Alex
            update Customer a536b743-416f-46a6-97e7-9261550dc94a measurements[Height] 180

        Arguments:
            class_name (str): Name of the class.
            instance_id (str): ID of the instance.
            attribute (str): Name of the attribute.
            value (str): Value to set.

        Note:
            - For updating attributes within the 'measurements' dictionary, use the format 'measurements[key]'.

        """
        parser = argparse.ArgumentParser()
        parser.add_argument('class_name', help='Name of the class')
        parser.add_argument('instance_id', help='ID of the instance')
        parser.add_argument('attribute', help='Name of the attribute')
        parser.add_argument('value', help='Value to set')

        args = parser.parse_args(shlex.split(arg))

        if args.class_name not in classes:
            print("** class doesn't exist **")
            return

        k = args.class_name + "." + args.instance_id
        if k not in models.storage.all():
            print("** no instance found **")
            return

        instance = models.storage.all()[k]

        # Check if the attribute is measurements[key]
        if args.attribute.startswith(
            'measurements[') and args.attribute.endswith(']'):
            key = args.attribute.split('[', 1)[1].rstrip(']')
            measurements = getattr(instance, 'measurements', {})
            measurements[key] = args.value
            setattr(instance, 'measurements', measurements)
        else:
            setattr(instance, args.attribute, args.value)

        instance.save()

    def do_count(self, arg):
        """
        Count the number of instances of a class.

        Usage:
            count ClassName

        Example:
            count User

        Arguments:
            ClassName (str): Name of the class.

        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name == "all":
            for cls_name, cls in classes.items():
                obj_dict = models.storage.all(cls)
                count = len(obj_dict)
                print(f"Number of instances of {cls_name}: {count}")
            return

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        obj_dict = models.storage.all(classes[class_name])
        count = len(obj_dict)
        print(f"Number of instances of {class_name}: {count}")

if __name__ == '__main__':
    # MBookCommand().cmdloop()
    try:
        MBookCommand().cmdloop()
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()