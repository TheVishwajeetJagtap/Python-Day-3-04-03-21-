char=input("Please enter a character: ")
if char>='A' and char<='Z':
    print(char," is an uppercase letter")
elif char>='a' and char<='z':
    print(char," is a lowercase letter")
else:
    print(char," is not in Alphabet")
