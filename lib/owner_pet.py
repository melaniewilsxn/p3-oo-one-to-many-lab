class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if self.check_pet_type(pet_type):
            self.name = name
            self.pet_type = pet_type
            self._owner = owner
            Pet.all.append(self)
        else:
            raise Exception
    
    @classmethod
    def check_pet_type(cls, pet_type):
        return pet_type in cls.PET_TYPES

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise TypeError
        self._owner = value

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError
        pet.owner = self
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)