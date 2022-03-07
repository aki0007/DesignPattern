"""
BDD pattern. Abstraction exists between an object that that invokes command and the object that performs it
"""
from abc import ABCMeta
import time


# Receiver
class Light:
    @staticmethod
    def switch_on():
        print("The light is on")

    @staticmethod
    def switch_off():
        print("The Light is off")


# ICommand Interface
class ICommand(metaclass=ABCMeta):
    @staticmethod
    def execute(self):
        """ A static interface method"""


# Command ON
class SwitchOnCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.switch_on()


# Command OFF
class SwitchOffCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.switch_off()


# Invoker
class Switch:
    """THe Invoker Class"""
    def __init__(self):
        self._commands = {}
        self._history = []

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
            self._history.append({time.ctime(int(time.time())): command_name})
        else:
            print("Command  not found")

    @property
    def history(self):
        return self._history


# Client
if __name__ == "__main__":
    # Receiver
    LIGHT = Light()

    # Commands
    SWITCH_ON = SwitchOnCommand(LIGHT)
    SWITCH_OFF = SwitchOffCommand(LIGHT)

    # Invoker
    SWITCH = Switch()

    # Register commands in the invoker
    SWITCH.register("ON", SWITCH_ON)
    SWITCH.register("OFF", SWITCH_OFF)

    SWITCH.execute("ON")
    SWITCH.execute("OFF")

    print(SWITCH.history)

