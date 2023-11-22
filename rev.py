class stringc:
    def reversew(self,s):
        return ''.join(reversed(s.split()))
s = input("Enter the string :")
print(stringc().reversew(s))