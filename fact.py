def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1);
print("The program is to find the factorial of a number")
n=int(input("Enter the number tofind the factorialof a given number: "))
print(50*'-')
print("The factorial of the given number is : ",fact(n))