import math
print('Please enter radius:')
radius = float(input())
circle_area1 = 3.14159265*radius*radius

circle_area2 = circle_area1/2
circle_area2_radius = circle_area2/3.14159265
circle_area2_radius_2 = math.sqrt (circle_area2_radius)
print("The radius of the second circle(aka the circle with half the area of circle 1)is",circle_area2_radius_2)






