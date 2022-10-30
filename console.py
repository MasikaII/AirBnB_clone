#!/usr/bin/python3
"""Contains the entry point of a command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the class definition for the command interpreter"""
    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
