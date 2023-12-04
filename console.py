#!/usr/bin/python3
""" Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when the line is empty"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl + D)"""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
