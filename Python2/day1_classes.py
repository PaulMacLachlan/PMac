class Pokemon(object):

    def __init__(self):
        self._species = "Pikachu"
        self.moves = ["thunderbolt", "quick attack", "thunder", "double dash"]

    def say_name(self):
        return self.species

    def get_name(self):
        return self.species

    def get_moveset(self):
        self.species = name

pikachu = Pokemon()
print pikachu.get_name()


class Pikachu(Pokemon):
    def __init__(self):
        pass
