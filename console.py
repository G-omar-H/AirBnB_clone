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

    cls_dict = {"BaseModel": models.BaseModel}
    prompt = "(hbnb)"
    dictt = models.storage.all()

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
            for key, value in self.cls_dict.items():
                if name == key:
                    Pixi = value()
                    Pixi.save()
                    print(Pixi.id)
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
            if args[0] in self.cls_dict.keys():
                if args[1] is not None:
                    name = "{}.{}".format(args[0], args[1])
                    for key, value in self.dictt.items():
                        if name == key:
                            print(value)
                            break
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
