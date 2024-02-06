class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        """
        Method to get a string from console input.
        """
        self.input_string = input("Enter a string: ")

    def printString(self):
        """
        Method to print the string in upper case.
        """
        print("String in upper case:", self.input_string.upper())

# Example usage:
string_manipulator = StringManipulator()
string_manipulator.getString()
string_manipulator.printString()