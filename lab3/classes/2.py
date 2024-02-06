class Shape:
    def __init__(self):
        pass

    def area(self):
        """
        Method to calculate and print the area of the shape.
        Default implementation returns 0.
        """
        print("Area of the shape: 0")


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        """
        Method to calculate and print the area of the square.
        """
        area_value = self.length ** 2
        print(f"Area of the square with length {self.length}: {area_value}")


# Example usage:
shape_instance = Shape()
shape_instance.area()  # This will print "Area of the shape: 0"

square_instance = Square(4)
square_instance.area()  # This will print "Area of the square with length 4: 16"