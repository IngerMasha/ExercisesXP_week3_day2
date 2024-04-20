class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
def fined_the_oldest_cat(cats):
        the_oldest_cat=Cat("None", 0)
        for cat in cats:
            if cat.age >the_oldest_cat.age:
                the_oldest_cat = cat
        return the_oldest_cat

def main():
    cat1 = Cat("Murca", 12)
    cat2 = Cat("Larisa", 6)
    cat3 = Cat("Loki", 2)
    the_oldest_cat = fined_the_oldest_cat([cat1, cat2, cat3])
    print(f"Exercise1: Cats\nThe oldest cat is {the_oldest_cat.name} , and is {the_oldest_cat.age} years old.")


if __name__=="__main__":
    main()


    # print("Exercise 4 : Afternoon At The Zoo")
    #
    #
    # class Zoo:
    #     def __init__(self, zoo_name):
    #         self.animals = []
    #         self.name = zoo_name
    #
    #     def add_animal(self, new_animal):
    #         if new_animal not in self.animals:
    #             self.animals.append(new_animal)
    #
    #     def get_animals(self):
    #         print(self.animals)
    #
    #     def sell_animal(self, animal_sold):
    #         if animal_sold in self.animals:
    #             self.animals.remove(animal_sold)
    #             self.get_animals()
    #
    #     def sort_animals(self):
    #         self.animals.sort()
    #         print(self.animals)
    #
    #
    # animals = ["Ape", "Baboon", "Bear", "Cat", "Cougar", "Eel", "Emu"]
    # ramat_gan_safari = Zoo("my_zoo")
    # for animal in animals:
    #     ramat_gan_safari.add_animal(animal)
    # ramat_gan_safari.get_animals()
    # ramat_gan_safari.add_animal(input("What animal you want to add? "))
    # ramat_gan_safari.sort_animals()
    # ramat_gan_safari.sell_animal(input("What animal you want to sell? "))
