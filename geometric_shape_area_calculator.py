#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print("Welcome to the geometric shape area calculator!")
    # User Options
    A = "Circle = 1"
    B = "Rectangle = 2"
    C = "Triangle = 3"
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print(A + " " + B + " " + C)
    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = int(input("Select a shape by entering 1, 2, 3"))
    # TODO: Convert the variable 'choice' to an integer data type.
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print(type(choice) == int)
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        radius = float(input("What is the raduis of the circle?"))
        # TODO: Convert 'radius' to float.
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = circle_pi * (radius ** 2)
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        length = float(input("What is the length of the rectangle?"))
        width = float(input("What is the width of the rectangle?"))
        # TODO: Convert both 'length' and 'width' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        area = length * width
        # HINT: The formula to find the area of a rectangle: length times width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        base = float(input("What is the base length of the triangle?"))
        height = float(input("What is the base height of the triangle?"))
        # TODO: Convert both 'base' and 'height' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        area = 0.5 * base * height 
        # HINT: The formula to find the area of a Triangle: half times base times height
    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print("Invalid choice .")
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
    print("Step 1: Cloned the repository to my local folder using git clone.")
    print("Step 2: Using the print function, I printed out 'Welcome to the geometric shape area calculator'.")
    print("Step 3: Defined user options A, B, and C as strings for the circle, rectangle, and triangle.")
    print("Step 4: Used string concatenation to print the user options as a single string with spaces.")
    print("Step 5: Prompted the user to select a shape by entering 1, 2, or 3 and assigned the input to the 'choice' variable.")
    print("Step 6: Converted the 'choice' variable to an integer data type using int().")
    print("Step 7: Verified that the 'choice' variable is indeed of the data type integer and printed the result.")
    print("Step 8: Implemented conditional logic to handle the user's choice and perform calculations for circles, rectangles, and triangles.")
    print("Step 9: Calculated the area of a circle based on the user's input of the radius.")
    print("Step 10: Calculated the area of a rectangle based on the user's input of the length and width.")
    print("Step 11: Calculated the area of a triangle based on the user's input of the base length and height.")
    print("Step 12: Added 'Invalid Choice .' message to handle invalid user inputs (choices other than 1, 2, or 3).")
    print("Step 13: Documented the code by adding comments to describe each section and step.")
    print("Step 14: Ran the unit test on the terminal and made sure it successfully passes.")
    print("Step 15: Pushed the updated code back to the main remote Git repository.")
    
if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY