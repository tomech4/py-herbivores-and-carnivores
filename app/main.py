class Animal:
    alive = []
    # include class instances, if health = 0, remove from the list

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive += self

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True

class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal):
        if (
                animal is Herbivore
                and animal.hidden is False
                and animal.health > 0
        ):
            animal.health -= 50