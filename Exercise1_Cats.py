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

