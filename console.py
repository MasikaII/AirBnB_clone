#!/usr/bin/python3
"""contains the entry point of a command interpreter"""
from cmd import Cmd
import uuid
from models import storage
from models.base_model import BaseModel

class HBNBCommand(Cmd):

    '''This is a class definition for the command processor'''
    prompt = '(hbnb)'

    def do_quit(self, line):
        '''This is a method to exit the program'''
        return True

    def do_EOF(self, line):
        '''This is a method to exit the command line'''
        return True

    def help_quit(self):
        '''Give information on the method quit'''
        print("Quit command to exit the program")

    def help_EOF(self):
        """this command quits the program"""
        return True

    def empty_line(self):
        """ when the line is empty print nothing"""
        pass

    """creating console commands"""
    def do_create(self, line):
        """this is the command to create new instances
        usage: create <name>"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.selected:
            print("** class doesn't exixt **")
        else:
            line = BaseModel()
            print(line.id)

    def do_show(self, line):
        """print the string representation of an
        instance based on the class name and id
        usage: show BaseModel 1234-1234-1234
        """
        all_objects = storage.all()
        if line:
            line = line.split()
            if len(line) == 1:
                print("** instance id missing **")
            elif len(line) >= 2:
                name = line[0]
                name_id = line[1]

                if name not in type(self).selected:
                    print("** class doesn't exist **")

                key_name = name + "." + name_id
                if key_name in all_objects.keys():
                    print(all_objects[key_name])
                else:
                    print("** no isntance found **")

            else:
                print("** class name missing **") 

        def do_destroy(self, line):
            """Deletes an instance based on class name and id 
            usage: destroy Basemodel 1234-1234-1234
            """
            all_objects = storage.all()

            if line:
                line = line.split()
                if len(line) == 1:
                    print("** instance id missing **")
                elif len(line) >= 2:
                    name = line[0]
                    name_id = line[1]

                    if name not in type(self).selected:
                        print("** class doesn't exist **")

                    key_name = name + "." + nmae_id
                    if key_name in all_objects.keys():
                        del all_objects[key_name]
                    else:
                        print("** no instance found **")

                else:
                    print("** class name missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
