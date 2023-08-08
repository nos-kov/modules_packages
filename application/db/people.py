class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    #def __str__(self):
      #  return f"{self.name} is {self.age} years old"

    def get_employees(self):

        return f"{self.name} is {self.age} years old"