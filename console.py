#!/usr/bin/python3
"""Contains the entry point of a command interpreter"""


import cmd
from datetime import datetime
import uuid
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This is the class definition for the command interpreter"""

    prompt = "(hbnb) "
    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"]

    def do_EOF(self, line):
        """ This is a method to exit the program"""
        return True

    def help_EOF(self):
        """ This helps to quit the program """
        print("This also quits program\n")

    def do_quit(self, line):
        """This is a method to quit the program"""
        return True

    def help_quit(self):
        """Gives more information on the method quit"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """when line is empty print nothing"""
        pass
        print("Quit command to exit the program")

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if line:
            if line in type(self).classes:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)

            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        all_objs = storage.all()
        if line:
            line = line.split()
            if len(line) == 1:
                if line[0] in type(self).classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(line) >= 2:
                name = line[0]
                name_id = line[1]
                obj_key = line[0] + "." + line[1]
                if obj_key in all_objs.keys():
                    str_instance = all_objs[obj_key]
                    print(str_instance)
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class nameand
        id (save the change into the JSON file)
        """
        all_objs = storage.all()
        if line:
            line = line.split()
            if len(line) == 1:
                if line[0] in type(self).classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")

            elif len(line) >= 2:
                name = line[0]
                name_id = line[1]
                obj_key = f"{line[0]}.{line[1]}"

                if obj_key in all_objs.keys():
                    del all_objs[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if line:
            all_objs = storage.all()
            line = line.split()
            if len(line) == 1:
                if line[0] in type(self).classes:
                    if all_objs:
                        for value in all_objs.values():
                            print(value)
                    else:
                        pass
                else:
                    print("** class doesn't exist **")
            else:
                pass
        else:
            pass

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        all_objs = storage.all()
        line = line.split()
        if line:
            if len(line) == 1:
                if line[0] == type(self).classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(line) == 2:
                key = line[0] + "." + line[1]
                if key in all_objs.keys():
                    print("** attribute name missing **")

                else:
                    print("** no instance found **")

            elif len(line) == 3:
                key = line[0] + "." + line[1]
                if key in all_objs.keys():
                    print("** value missing **")
                else:
                    print("** no instance found **")

            elif len(line) >= 4:
                key = line[0] + "." + line[1]
                if key in all_objs.keys():
                    new_instance = all_objs[key].to_dict()
                    attribute_key = line[2]
                    attribute_value = line[3]
                    new_instance[attribute_key] = attribute_value
                    new_inst_obj = BaseModel(**new_instance)
                    new_inst_obj.save()
                    storage.new(new_inst_obj)

                else:
                    print("** no instance found **")

        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
