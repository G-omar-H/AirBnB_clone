#!/usr/bin/python3
"""
entry point programme to the command interpreter
"""
import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """
    console class defining for the AirBnb project foundation
    """

    cls_dict = {"BaseModel": models.BaseModel}
    prompt = "(hbnb)"
    obj_dict = models.storage.all()

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
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = line.split(" ")
        if len(args) > 0:
            if args[0] in self.cls_dict.keys():
                if len(args) > 1:
                    name = "{}.{}".format(args[0], args[1])
                    for key, value in self.obj_dict.items():
                        if name == key:
                            flag = 1
                            print(value)
                            break
                        flag = 0
                    if flag == 0:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        destroy: Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = line.split(" ")
        if len(args) > 0:
            if args[0] in self.cls_dict.keys():
                if len(args) > 1:
                    name = "{}.{}".format(args[0], args[1])
                    for key, value in self.obj_dict.items():
                        if name == key:
                            flag = 1
                            del value
                            models.storage.save()
                            break
                        flag = 0
                    if flag == 0:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        if line and line not in self.cls_dict.keys():
            print("** class doesn't exist **")
            pass
        else:
            all_list = []
            for value in self.obj_dict.values():
                all_list.append(value.__str__())
            print(all_list)

    def do_update(self, line):
        """
        update: Updates an instance based on the class name and id by adding
            or updating attribute (save the change in  to the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = line.split(" ")
        print(args)
        if len(args) > 0:
            if args[0] in self.cls_dict.keys():
                if len(args) > 1:
                    name = "{}.{}".format(args[0], args[1])
                    for key, value in self.obj_dict.items():
                        if name == key:
                            name_value = value
                            print(name_value)
                            flag = 1
                            break
                        flag = 0
                    if flag == 0:
                        print("** no instance found **")
                        return
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(name_value, args[2], args[3])
                            models.storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print(" ** attribute name missing **")
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
