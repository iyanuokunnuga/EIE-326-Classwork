import math

def circle_area(radius):
    return math.pi * radius * radius

def cone_surface_area(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * (radius + slant_height)

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def sector_area(radius, angle):
    area = math.pi * radius * radius * (angle / 360)
    return area

radius = 6
height = 7.5
angle = 60

print(f"Area of circle with radius {radius} is: {circle_area(radius)}")
print(f"Surface area of cone with radius {radius} and height {height} is: {cone_surface_area(radius, height)}")
print(f"Surface area of cylinder with radius {radius} and height {height} is: {cylinder_surface_area(radius, height)}")
print(f"Area of sector of circle with radius {radius} and angle {angle} degrees is: {sector_area(radius, angle)}")