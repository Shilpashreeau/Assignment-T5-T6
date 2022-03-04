#Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits”
x=input("enter 4 digit number\n")
try:
    if len(x)>4 or len(x)<4:
        raise Exception
except:
    print("length is too short/long")

else:
    print("you entered right")

   