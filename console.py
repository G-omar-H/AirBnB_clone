#!/usr/bin/python3
"""
entry point programme to the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    console class defining for the AirBnb project foundation
    """

    prompt = "(hbnb)"

    def emptyline(self):
        pass

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
