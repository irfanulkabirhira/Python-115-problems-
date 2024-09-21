# 62. List of Tuples Conversion: Given a nested list containing tuples of (x, y) coordinates, write a Python program to convert it into a list of x-coordinates and a list of y-coordinates.

# Function to convert a nested list of (x, y) tuples into separate x and y coordinate lists
def convert_coordinates(nested_list):
    x_coords = []
    y_coords = []
    
    for sublist in nested_list:
        for (x, y) in sublist:
            x_coords.append(x)
            y_coords.append(y)
    
    return x_coords, y_coords

# Taking a nested list of (x, y) tuples as input from the user
# For simplicity, we assume the input is a string representing the nested list
print("Enter a nested list of (x, y) tuples (e.g., [[(1, 2), (3, 4)], [(5, 6)]]) :")
input_str = input()
nested_list = eval(input_str)

# Converting the coordinates
x_coords, y_coords = convert_coordinates(nested_list)

# Output the x-coordinates and y-coordinates
print("List of x-coordinates:")
print(x_coords)
print("List of y-coordinates:")
print(y_coords)
