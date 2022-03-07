"""
Singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance.
This is useful when exactly one object is needed to coordinate actions across the system
"""


from abc import ABCMeta


class IPerson(metaclass=ABCMeta):
    @staticmethod
    def get_data():
        """ Implement in child class"""


class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more then once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name is {PersonSingleton.__instance.name}, age is {PersonSingleton.__instance.age}")


p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()
