# from abc import ABC, abstractmethod


class Band:
    all_bands = []

    def __init__(self, name="none", members=[]):
        self.name = name
        self.members = members
        Band.all_bands.append(self)

    def __str__(self):
        greeting = f"{self.name}"
        return greeting

    def __repr__(self):
        declaration = f"{self.name}"
        return declaration

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return Band.all_bands


class Musician:
    members = []

    def __init__(self, name="none"):
        self.name = name

    @staticmethod
    def __str__():
        pass

    @staticmethod
    def __repr__():
        pass

    @staticmethod
    def get_instrument():
        pass

    @staticmethod
    def play_solo():
        pass


class Guitarist(Musician):
    """"Guitarist instance. Name = Joan Jett"""
    def __str__(self):
        greeting = f"My name is {self.name} and I play guitar"
        return greeting

    def __repr__(self):
        declaration = f"Guitarist instance. Name = {self.name}"
        return declaration

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return f"face melting guitar solo"


class Bassist(Musician):
    def __str__(self):
        greeting = f"My name is {self.name} and I play bass"
        return greeting

    def __repr__(self):
        declaration = f"Bassist instance. Name = {self.name}"
        return declaration

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return f"bom bom buh bom"


class Drummer(Musician):
    def __str__(self):
        greeting = f"My name is {self.name} and I play drums"
        return greeting

    def __repr__(self):
        declaration = f"Drummer instance. Name = {self.name}"
        return declaration

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return f"rattle boom crash"

# bob = Guitarist("Bob")
# print(bob)
# nirvana = Band("Nirvana", ["curk", "bob", "joe"])
# print(Band.to_list())