#Allison Wiseman CIS261 Rectangle
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def get_perimeter(self):
        return 2 * (self.height + self.width)
    
    def get_area(self):
        return self.height * self.width
    
    def print_rectangle(self):
        for i in range(self.height):
            if i == 0 or i == self.height -1:
                print("*" * self.width)
            else:
                print("*" + " " * (self.width - 2) + "*")
                
while True:
    print("\nRectangle Calculator")
    
    try:
        height = int(input("Height: "))
        width = int(input("Width: "))
        
        if height <= 0 or width <= 0:
            print("Please enter positive integers for height and width.")
            continue
    
        rect = Rectangle(height, width)
    
        print("Perimeter:", rect.get_perimeter())
        print("Area:", rect.get_area())
        rect.print_rectangle()
        
    except ValueError:
        print("Invalid input, please enter integer values.")
        
    choice = input("\nContinue? (y/n): ").strip().lower()
    if choice != 'y':
        break
    
