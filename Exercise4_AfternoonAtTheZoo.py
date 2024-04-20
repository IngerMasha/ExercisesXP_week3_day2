class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            self.get_animals()

    def sort_animals(self):
        self.animals.sort()
        print(self.animals)


def main():
    animals = ["Ape", "Baboon", "Bear", "Cat", "Cougar", "Eel", "Emu"]
    ramat_gan_safari = Zoo("my_zoo")
    for animal in animals:
        ramat_gan_safari.add_animal(animal)
    ramat_gan_safari.get_animals()
    ramat_gan_safari.add_animal(input("What animal you want to add? "))
    ramat_gan_safari.sort_animals()
    ramat_gan_safari.sell_animal(input("What animal you want to sell? "))
if __name__=="__main__":
    main()