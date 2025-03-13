print("Please enter three positive integers:")
num1=int(input())
num2=int(input())
num3=int(input())
if(num1<num2<num3):
    print(num1,"is smaller than",num2,"is smaller than",num3)
elif(num1<num3<num2):
    print(num1,"is smaller than",num3,"is smaller than",num2)
elif(num2<num1<num3):
    print(num2,"is smaller than",num1,"is smaller than",num3)
elif(num2<num3<num1):
    print(num2,"is smaller than",num3,"is smaller than",num1)
elif(num3<num2<num1):
    print(num3,"is smaller than",num2,"is smaller than",num1)
else:
    print(num3,"is smaller than",num1,"is smaller than",num2)
    
