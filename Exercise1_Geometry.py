class Circle:
    def __init__(self, radius=10):
        self.radius = radius

    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2)

    def area(self):
        return round(3.14 * (self.radius ** 2), 2)

    def print_definition(self):
        print(
            "A circle is a round-shaped figure that has no corners or edges. In geometry, a circle can be defined as a closed shape, two-dimensional shape,curved shape.")


def main():
    circle1 = Circle()
    print("Perimeter:", circle1.perimeter())
    print("Area:", circle1.area())
    circle1.print_definition()

    circle2 = Circle(3)
    print("\nPerimeter:", circle2.perimeter())
    print("Area:", circle2.area())
    circle2.print_definition()


if __name__ == "__main__":
    main()
