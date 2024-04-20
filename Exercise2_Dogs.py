# print("Exercise2: Dogs")
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jump {self.height} cm height")
    def __str__(self):
        return f"Dog's name: {self.name}, it's height: {self.height}"
def main():
    davids_dog = Dog("Rex", 50)
    print(davids_dog)
    davids_dog.bark()
    davids_dog.jump()
    sarahs_dog = Dog("Teacup", 20)
    print(sarahs_dog)
    sarahs_dog.bark()
    sarahs_dog.jump()
    print(f"The biggest dog is {davids_dog.name if davids_dog.height>sarahs_dog.height else sarahs_dog.name}")


if __name__=="__main__":
    main()