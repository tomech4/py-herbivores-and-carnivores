class Animal:
    alive = []
    # include class instances, if health = 0, remove from the list

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True
