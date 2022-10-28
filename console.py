#!/usr/bin/python3
from cmd import Cmd
import uuid
from datetime import datetime

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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
