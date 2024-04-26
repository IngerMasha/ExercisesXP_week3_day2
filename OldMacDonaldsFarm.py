class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal, count=1):
        for a in self.animals:
            if a["name"] == animal:
                a["count"] += count
                break
        else:
            temp = {
                "name": animal,
                "count":count
            }
            self.animals.append(temp)

    def get_info(self):
        result = f"{self.name}'s farm\n\n"
        for i in range(len(self.animals)):
            result += self.animals[i]['name'] + " : " + str(self.animals[i]['count']) + '\n'
        result += "\n    E-I-E-I-0!"
        return result

    def get_animal_types(self):
        names = [animal["name"] for animal in self.animals]
        names.sort()
        return names

    def get_short_info(self):
        result = f"{self.name}’s farm has "
        names = self.get_animal_types()
        for i in range(len(names)):
            result += names[i] + "s"
            if i < len(names) - 1:
                result += ", "
        result += '.'
        return result



def main():
    macdonald = Farm("McDonald")
    macdonald.add_animal('cow', 5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)
    print(macdonald.get_info())
    print(macdonald.get_short_info())
    macdonald.add_animal('chicken', 10)
    print(macdonald.get_short_info())

if __name__ == "__main__":
    main()
