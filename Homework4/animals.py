from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, leg_count):
        self.name = name
        self.age = age
        self.leg_count = leg_count

    @abstractmethod
    def to_string():
        pass

    @staticmethod
    @abstractmethod
    def to_communicate():
        pass

    @staticmethod
    @abstractmethod
    def can_fly():
        pass

