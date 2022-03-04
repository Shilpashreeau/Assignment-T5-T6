#Write a program in Python to find out the character in a string which is uppercase using list
#comprehension.
# 1 way
x=[i for i in "shIlpa" if i.isupper()]
print(x)

# 2nd way
y=input("enter the string\n")
z=[i for i in y if i.isupper()]
print(z)