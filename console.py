#!/usr/bin/python3
"""
entry point programme to the command interpreter
"""
import cmd
import models
import sys


class HBNBCommand(cmd.Cmd):
    """
    console class defining for the AirBnb project foundation
    """

    cls_dict = {
        "BaseModel": models.BaseModel,
        "User": models.User,
        "State": models.State,
        "City": models.City,
        "Amenity": models.Amenity,
        "Place": models.Place,
        "Review": models.Review,
    }
    prompt = "(hbnb) "
    obj_dict = models.storage.all()
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

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
                    return
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
        arglist = [arg for arg in args if arg != ""]
        flag = 0
        if line:
            if arglist[0] in self.cls_dict.keys():
                if len(arglist) > 1:
                    name = "{}.{}".format(arglist[0], arglist[1])
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

    def do_count(self, arg):
        """
        count number of instances if a class
        """
        count = 0
        for k, v in self.obj_dict.items():
            name = k.split(".")[0]
            if arg == name:
                count += 1
        print(count)

    def do_destroy(self, line):
        """
        destroy: Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        arglist = line.split(" ")
        args = [arg for arg in arglist if arg != ""]
        flag = 0
        if line:
            if args[0] in self.cls_dict.keys():
                if len(args) > 1:
                    name = "{}.{}".format(args[0], args[1])
                    for key, value in self.obj_dict.items():
                        if name == key:
                            flag = 1
                            del models.storage.all()[key]
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

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        all_list = []
        if args:
            if args not in self.cls_dict:
                print("** class doesn't exist **")
                return
            for k, v in models.storage.all().items():
                if args == type(v).__name__:
                    all_list.append(str(v))
        else:
            for key, value in self.obj_dict.items():
                all_list.append(str(value))
        print(all_list)

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def do_update(self, line):
        """
        update: Updates an instance based on the class name and id by adding
            or updating attribute (save the change in  to the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        arglist = line.split(" ")
        args = [arg for arg in arglist if arg != ""]
        flag = 0
        if line:
            if args[0] in self.cls_dict.keys():
                if len(args) > 1:
                    name = "{}.{}".format(args[0], args[1])
                    for key, value in self.obj_dict.items():
                        if name == key:
                            obj_value = value
                            flag = 1
                            break
                        flag = 0
                    if flag == 0:
                        print("** no instance found **")
                        return
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[3][0] in ["'", '"']\
                                    and args[3][-1] in ["'", '"']:
                                setattr(obj_value, args[2], args[3][1:-1])
                            else:
                                if args[3].isdigit():
                                    setattr(obj_value, args[2], int(args[3]))
                                elif self.isfloat(args[3]):
                                    setattr(obj_value, args[2], float(args[3]))
                                else:
                                    setattr(obj_value, args[2], args[3])
                            obj_value.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
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
