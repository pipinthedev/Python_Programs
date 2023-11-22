n = int(input("Enter the max value :"))
even = 0
odd = 0
for number in range(1,n+1):
    if (number%2==0):
        even+=1
    else:
        odd+=1
print(even,odd)