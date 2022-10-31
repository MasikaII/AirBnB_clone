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
    def do_create(self, line):
        """
        this command is for creation of new instances
        usage: create <name>
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.selected:
            print("** class doesn't exist **")
        else:
            line = BaseModel()
            print(line.id)

        def do_show(self, line):
            """print the string representation of an instance
            based on thethe class name and nd id
            usage: show BaseModel 1234-1234-1234
            """
            all objects = storage.all()

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
                    del all_objects[key_name]
                else:
                    print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
