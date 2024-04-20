import random


class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse_list(self):
        return list(reversed(self.letters))

    def sorted_list(self):
        return sorted(self.letters)

    def generate_random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]
def main():
    letters = ['e','k', 'b','l', 'c', 'd', 'a']
    my_list = MyList(letters)
    print(letters)
    reversed_list = my_list.reverse_list()
    print("Reversed List:", reversed_list)
    sorted_list = my_list.sorted_list()
    print("Sorted List:", sorted_list)
    random_list = my_list.generate_random_list()
    print("Random List:", random_list)

if __name__ == "__main__":
    main()