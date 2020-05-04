class Owner:

    def __init__(self, name, computers=[]):
        self.name = name
        self.computers = computers
        #self.location = location

    def __repr__(self):
        repr_string = f"{self.name.upper().ljust(20)}\n\n"
        repr_string += '\n'.join(str(x) for x in self.computers)
        return (repr_string)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def computers(self):
        return self.__computers

    @computers.setter
    def computers(self, computers):
        self.__computers = computers

    def add_computer(self, computer):
        self.computers.append(computer)
