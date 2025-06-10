#Defining the Function
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# Welcome Message
print ("Let's find factorial of any small integer:")

#Input from User
x = int(input("Enter any non negative integer:"))

#Output
result=factorial(x)
print("Factorial of", x ,"is",result)