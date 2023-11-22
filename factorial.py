def fact(n):
    if n == 1: 
     return 1
    elif n>1:
       return n*fact(n-1)
n = int(input("Enter the number:"))
print("Factorail of that number is",fact(n))