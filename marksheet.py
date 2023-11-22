n = int(input("Enter total subjects :"))
total = 0
for i in range(1,n+1):
    print("Enter the",str(i),"mark")
    m = int(input())
    total=int(total)+m
print("Total",total)
avg = total/n
if avg>=80: 
 print ("Grade A") 
elif avg>=70 and avg<80: 
 print ("Grade B") 
elif avg>=60 and avg<70: 
 print ("Grade C") 
elif avg>=40 and avg<60: 
 print ("Grade D") 
elif avg<40 : 
 print("Grade E") 
else: 
 print ("Fail")