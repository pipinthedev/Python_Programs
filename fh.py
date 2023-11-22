chi = int(input("Enter the option"))
if chi == 1:
    f = int(input("Enter the fahernheit: "))
    c = (f-32)*5/9
    print("Celcius : ",c)
elif chi == 2:
    c = int(input("Enter the celcius: "))
    f = 9/5*(c+32)
    print("Fahernheit : ",f)
else:
    print("Invaild choice")