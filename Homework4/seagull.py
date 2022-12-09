from animals import Animal

class Seagull(Animal):
    def __int__(self, name, age, leg_count):
        super().__init__(name, age, leg_count)

    def to_string(self):
        return {
            "name":self.name,
            "age":self.age,
            "leg_count":2
        }

    @staticmethod
    def to_communicate():
        return "I am human,and I can fly"

    @staticmethod
    def can_fly():
        return True