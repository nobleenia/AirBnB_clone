#!/usr/bin/python3
"""
Command-line interface (CLI) for managing application objects

The available classes for object management are:
- BaseModel
- State
- City
- Amenity
- Place
- Review
- User
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    `HBNBCommand` class provides CLI for managing objects of various classes
    """
    prompt = "(hbnb) "
    class_dict = {
        "BaseModel",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
        "User"
    }

    def do_quit(self,arg):
        """
        Command: quit
        Exit the command-line interface

        Args:
            arg (str): Ignored

        Returns:
            bool: True to exit the CLI
        """
        return True

    def do_EOF(self, arg):
        """
        Command: EOF
        Exit the CLI upon receiving an EOF signal (e.g., Ctrl+D)

        Args:
            arg (str): Ignored

        Returns:
            bool: True to exit the CLI
        """
        print("")
        return True

    def emptyline(self):
        """
        Command: <empty line>
        Do nothing when an empty line is entered

        Args:
            None

        Returns:
            None
        """
        pass

    def do_create(self, arg):
        """
        Command: create <class_name>
        Create an instance of a specified class and print its ID

        Args:
            arg (str): class name for which an instance is created

        Example usage:
        $ create BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Command: show <class_name> <instance_id>
        Print the string representation of an instance based on the class name and ID

        Args:
            arg (str): The command argument in the format "class_name instance_id".

        Example usage:
        $ show BaseModel 1234-1234-1234
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                class_name = "{}.{}".format(args[0], args[1])
                if class_name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[class_name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
        Command: destroy <class_name> <instance_id>
        Delete an instance based on the class name and ID

        Args:
            arg (str): The command argument in the format "class_name instance_id"

        Example usage:
        $ destroy BaseModel 1234-1234-1234
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                class_name = "{}.{}".format(args[0], args[1])
                if class_name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del(storage.all()[class_name])
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """
        Command: all [<class_name>]
        Print all instances or instances of a specific class.

        Args:
            arg (str): The class name (optional) to filter instances.

        Example usage:
        $ all
        $ all BaseModel
        """
        args = arg.split()
        obj_print = []

        if args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        if len(arg) == 0:
            for objects in storage.all().values():
                obj_print.append(objects)
            print(obj_print)
        elif args[0] in HBNBCommand.class_dict:
            for key, objects in storage.all().items():
                if args[0] in key:
                    obj_print.append(objects)
            print(obj_print)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = arg.split()
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """
        Default handler for interpreting and executing commands based on the argument provided.

        Args:
        - self: Instance of the class containing this method.
        - arg: A string containing the command to be interpreted and executed.

        Returns:
        - If the command is recognized and executed, it returns the result of the executed command.
        - If the command is not recognized, it prints a message and returns
        """
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(args[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_update(self, arg):
        """
        Command: update <class_name> <instance_id> <attribute_name> "<attribute_value>"
        Update the attribute of an instance based on the class name, ID, attribute name, and new attribute value.

        Args:
            arg (str): The command argument in the format
                       "class_name instance_id attribute_name attribute_value".

        Example usage:
        $ update BaseModel 1234-1234-1234 name "New Name"
        """
        args = arg.split()

        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
