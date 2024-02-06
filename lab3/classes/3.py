class Shape:
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        """
        Method to calculate and print the area of the rectangle.
        """
        area_value = self.length * self.width
        print(f"Area of the rectangle with length {self.length} and width {self.width}: {area_value}")


# Example usage:
rectangle_instance = Rectangle(5, 8)
rectangle_instance.area()  # This will print "Area of the rectangle with length 5 and width 8: 40"
