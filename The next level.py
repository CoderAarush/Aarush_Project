def function(problem_type):
        if(problem_type== 1):
         print("Please enter the two variables")
         var = float(input())
         var2 = float(input())
         sum = var2 + var
         print(sum)
         return sum
        elif(problem_type == 2):
         print("Please enter the two variables")
         var2= float(input())
         var = float(input())
         sum = var2 - var
         print(sum)
         return sum
        elif(problem_type == 3):
         print("Please enter the two variables")
         var = float(input())
         var2 = float(input())
         sum = var2 * var
         print(sum)
         return sum
        else:
         print("Please enter the two variables")
         var = float(input())
         var2 = float(input())
         product = var/var2
         print(var,"divided by", var2,"is equal to",product)
         return product
def main():
 print("Please enter your problem type (addition = 1, subtraction = 2, multiplication = 3, division = 4,(first > sec)")
 problem_type = input()
 function(problem_type)




main()