import math
def solve(par_1):
    if(par_1 == 1):
        print("Please enter radius")
        r = float(input())
        circle_area = r*3.14285714
        circle_circumference = 2*3.14285714*r
        print("The area and circumference of the circle =",circle_area,"is the area",circle_circumference,"is circum")
    else:
        print("Please enter length and breath")
        l = float(input())
        b = float(input())
        rect_area = l*b
        rect_perimeter = 2*(l + b)
        print("The area and perimeter of the rectangle =",rect_area,"is the area",rect_perimeter,"is the perimeter")
def solve2(par_2):
    print("Please enter type of triangle - equilateral = 1, right angle triangle = 2")
    n = int(input())
    print("Please enter base and height of the triangle")
    b = float(input())
    h = float(input())
    if(n == 1):
        area = 0.5*b*h
        perimeter = 3*b
        print("Area and perimeter of the triangle =",area,"is area",perimeter,"is perimeter")
    else:
        area = 0.5*b*h
        s = math.sqrt(b*b + h*h)
        perimeter2 = s + b + h
        print("Area and perimeter of the triangle =",area,"is area",perimeter2,"is perimeter")



def main():
    print("Please enter problem type (a and p of circle,1;of rectangle,2;of triangle,3)")
    problem_type = int(input())
    if(problem_type == 1):
        solve(problem_type)
    elif(problem_type == 2):
        solve(problem_type)
    else:
        solve2(problem_type)
main()



