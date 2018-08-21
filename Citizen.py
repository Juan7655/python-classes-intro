from Person import Person


class Citizen(Person):
    def __init__(self, name, nationality):
        super().__init__(name)
        self.nationality = nationality

    def __str__(self):
        return super().__str__() + ", and comes from {}".format(self.nationality)
