from animals import Animal

class Dog(Animal):
    def __int__(self, name, age, leg_count):
        super().__init__(name, age, 4)

    def to_string(self):
        return {
            "name":self.name,
            "age":self.age,
            "leg_count":4
        }

    @staticmethod
    def to_communicate():
        return "I am dog, so I can bark"

    @staticmethod
    def can_fly():
        return False


