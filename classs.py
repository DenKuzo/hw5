class Hero:
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti


class Super_Hero(Hero):
    def __str__(self):
        print(f'{self.name} it is super_hero')