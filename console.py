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
        """Do nothing when line is empty"""
        pass

    """Creating the console commands"""
    def do_create(self, line):
        """This is the command to create new instances
        and saves it (to the JSON file)
        Usage: create <name>"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.selected:
            print("** class doesn't exist **")
        else:
            line = eval(line)()
            line.save()
            print(line.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id
        usage: show BaseModel 1234-1234-1234
        """
        all_objects = storage.all()

        if line:
            line = line.split()
            if len(line) == 1:
                print("** instance id missing **")
            elif len(line) == 2:
                name = line[0]
                name_id = line[1]

                if name not in type(self).selected:
                    print("** class doesn't exist **")

                key_name = name + "." + name_id
                if key_name in all_objects.keys():
                    print(all_objects[key_name])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on class name and id
        usage: destroy BaseModel 1234-1234-1234
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
                    del all_objects[key_name]
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """ Prints all string representation of all instances
            Usage: all BaseModel
        """
        all_objects = storage.all()
        if line:
            line = line.split()
            if line[0] in type(self).selected:
                if all_objects:
                    for key, value in all_objects.items():
                        print(value)
                else:
                    pass
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Usage: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        all_objects = storage.all()
        if line:
            line = line.split()
            if len(line) == 1 and line[0] not in type(self).selected:
                print("** class doesn't exist**")

            elif len(line) == 2:
                key_name = line[0] + "." + line[1]
                if key_name not in all_objects.keys():
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            elif len(line) == 3:
                key_name = line[0] + "." + line[1]
                if key_name in all_objects.keys():
                    print("** value missing **")
                else:
                    print("** no instance found **")
            elif len(line) >= 4:
                key_name = line[0] + "." + line[1]
                if key_name in all_objects.keys():
                    update_obj = all_objects[key_name]
                    update_to_dict = update_obj.to_dict()
                    class_name = update_to_dict["__class__"]
                    update_to_dict[line[2]] = line[3]
                    new_object = eval(class_name)(**update_to_dict)
                    new_object.save()
                    storage.new(new_object)

                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")



if __name__ == "__main__":
    HBNBCommand().cmdloop()
