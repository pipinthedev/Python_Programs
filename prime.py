n = int(input("Enter the range :"))
for numb in range(2, n + 1):
 if numb > 1:
  for a in range(2, numb):
     if (numb % a) == 0:
      break
  else:
     print(numb)