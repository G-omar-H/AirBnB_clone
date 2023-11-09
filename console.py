#!/usr/bin/python3
"""
entry point programme to the command interpreter
"""
import cmd, sys
import models

class HBNBCommand(cmd.Cmd):
    """
    console class defining for the AirBnb project foundation
    """

    list = ["BaseModel"]
    prompt = "(hbnb)"

    def emptyline(self):
        pass

    def do_create(self, name):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and
        prints the id. 
        Ex: $ create BaseModel
        """
        if name:
            print(type(models.BaseModel()).__name__)
            if name == type(models.BaseModel()).__name__:
                name = models.BaseModel()
                name.save()
                print(name.id)
            else :
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance 
        based on the class name and id. 
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = list(cmd.Cmd.parseline(self, line))
        if args[0] is not None:
            name = args[0]
            print(name)
            if name == type(models.BaseModel()).__name__:
                if args[1]:
                    name_id = args[1]
                    print(name_id)
                    if name_id == name.__class__.id:
                        print(name)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        End programm's process to exit
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
