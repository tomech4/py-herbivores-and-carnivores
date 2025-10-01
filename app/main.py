class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive += self

    @classmethod
    def __str__(cls):
        return [
            {
                "Name": animal.name,
                "Health": animal.health,
                "Hidden": animal.hidden
            }
            for animal in cls.alive
        ]

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

        if animal.health == 0:
            Animal.alive.remove(animal)
