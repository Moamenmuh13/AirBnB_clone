#!/usr/bin/python3
""" Console module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Command interpreter class.
    Attributes:
        prompt : The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "City", "Place", "Review", "State",
                 "Amenity"}

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        and save it to json file.
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand().__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instaces = storage.all()
            if key not in instaces:
                print("** no instance found **")
            else:
                print(instaces[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand().__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instaces = storage.all()
            if key not in instaces.keys():
                print("** no instance found **")
            else:
                del instaces[key]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of allall
        instances based or not on the class name.
        """
        args = arg.split()
        if args and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            listOfModels = []
            for model in storage.all().values():
                if not args or args[0] == model.__class__.__name__:
                    listOfModels.append(str(model))
            print(listOfModels)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does'nt exist **")
        elif len(args) == 1:
            print("** instace id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            try:
                value = eval(args[2])
            except NameError:
                print("** value missing **")
        else:
            instance = storage.all()["{}.{}".format(args[0], args[1])]
            attributeName = args[2]
            value = args[3]

            if attributeName not in ("id", "created_at", "updated_at"):
                if attributeName in instance.__class__.__dict__:
                    attrType = type(instance.__class__.__dict__[attributeName])
                    try:
                        castedValue = attrType(value)
                        setattr(instance, attributeName, castedValue)
                        instance.save()
                    except ValueError:
                        print("** invalid value **")
                else:
                    # Add the attribute to the class with the specified value
                    attrType = type(value)
                    setattr(instance.__class__, attributeName, attrType)
                    setattr(instance, attributeName, value)
                    instance.save()
            else:
                print("** cannot update id, created_at, or updated_at **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
