from .Computer import *

class Owner:

    def __init__(self, name: str, computers = []):
        self.name = name
        self.computers = computers
        #self.location = location

    def __repr__(self) -> str:
        repr_string = f"{self.name.upper().ljust(20)}\n\n"
        repr_string += '\n'.join(str(x) for x in self.computers)
        return (repr_string)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
        
    @property
    def computers(self):
        return self.__computers

    @computers.setter
    def computers(self, computers):
        self.__computers = computers

    def add_computer(self, computer: Computer):
        self.computers.append(computer)
