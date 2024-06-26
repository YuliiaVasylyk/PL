from .figure import *

# Function to get user input for the character representing the shape
def get_character_input():
    while True:
        character = input("Enter a character to represent in the shape: ")
        if Figure3D.is_appropriate_character(character) is False:
            print("You should have entered one character!")
        else:
            return character

# Function to get user input for the color position
def get_color_position_input():
    while True:
        try:
            color = int(input("Enter a number of color: "))
            if color not in range(len(colors)):
                print("You should have entered a color option which is available!")
            else:
                return color
        except ValueError:
            print("You should have entered an integer number!")

# Function to get user input for the length of the figure
def get_length_input():
    while True:
        try:
            length = int(input("Enter a length: "))
            if length <= 0:
                print("You should have entered a length greater than 0!")
            else:
                return length
        except ValueError:
            print("You should have entered an integer number!")

# Function to get user input for the scale of the figure
def get_scale_input():
    while True:
        try:
            scale = float(input("Enter a scale for the figure: "))
            if scale <= 0:
                print("You should have entered a scale greater than 0!")
            else:
                return scale
        except ValueError:
            print("You should have entered a float number!")

# Define a file to save 3D representation
representation_3d_file = "cube.txt"

# Main function to interact with the user and create 3D figures
def main():
    is_figure_available: bool = False
    is_3d_representation_available = False

    while True:
        print("1 - Create a cube")
        print("2 - Display 2D")
        print("3 - Save 3D")
        print("0 - Exit")
        option = str(input("Enter an option: "))

        match option:
            case "1":
                character = get_character_input()
                print("There are such colors available:")
                display_colors()
                color_position = get_color_position_input()
                length = get_length_input()
                scale = get_scale_input()
                try:
                    figure = Cube(length, character, color_position)
                    is_figure_available = True
                    representation_3d = figure.get_3d_representation(scale=scale)
                    print(representation_3d)
                    is_3d_representation_available = True
                except ValueError as e:
                    print(e)
                    is_figure_available = False
            case "2":
                if is_figure_available is True:
                    representation_2d = figure.get_2d_representation()
                    [print(item) for item in representation_2d]
                else:
                    print("There is no figure available!")
            case "3":
                if is_3d_representation_available is True:
                    try:
                        with open(representation_3d_file, "w") as file:
                            file.write(representation_3d)
                    except PermissionError:
                        print("You do not have permission to write to the file!")
                    except FileNotFoundError:
                        print("The file does not exist!")
                else:
                    print("There is no figure available!")
            case "0":
                break
            case _:
                print("Invalid option!")

if __name__ == "__main__":
    main()