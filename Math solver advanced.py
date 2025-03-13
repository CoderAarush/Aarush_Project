print("Please enter radius of circle 1:")
r1 = float(input())
print("Please enter radius of circle 2")
r2 = float(input())

circle_area_1 = (3.14159265*r1*r1)/2
circle_area_2 = (3.14159265*r2*r2)/2
total_area_half = circle_area_1 + circle_area_2
print("Therefore , half the area of circle 1 plus half the area of circle 2 = ", total_area_half)