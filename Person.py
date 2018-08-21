class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return "my name is " + self.name

    def __str__(self):
        return "The Person is named {}".format(self.name)
