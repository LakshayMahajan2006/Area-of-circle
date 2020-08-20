# Area-of-circle
# Lets create a program to give area of circle.

#Define a function to calculate radius.
def calculate_radius(rad):
    radius = float(rad)
    area = 3.14 * radius * radius
    print(f"The area of circle is {area}")

print("Click * to close program. \nEnter any radius.")

run = True

while run:
    rad = input("Enter radius of circle : ")
    if rad == '*':
        break
    calculate_radius(rad)
