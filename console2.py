#!/usr/bin/python3
from cmd import Cmd
import uuid
from datetime import datetime
#import
class HBNBCommand(cmd.Cmd):
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

    def create(self):
        new_model = Basemodel()
        new_model.save()
        print(id)
        if new_model.__class__.__name__ is missing:
            print("** class name missing **")
        if new_model.__class__.__name__ doesnt exist:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
