print ("Please enter perimeter of a rectangle and the difference between the length and the breadth")
perimeter = int(input())
difference = int(input())

length = (perimeter + difference)/2
breath = length - difference
rec_area = length * breath
print ("The area of a rectangle with", perimeter,"and difference between l and b = ", difference,"is", rec_area)