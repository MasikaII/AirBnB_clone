#!/usr/bin/python3
"""contains the entry point of a command interpreter"""
from cmd


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
