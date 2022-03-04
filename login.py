#Create a login page backend to ask users to enter the username and password. Make sure to
#ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
#should not be more than 3 times.
ip1=input("please enter username\n")
ip2=input("please enter password\n")
counter=0
while(counter<3):
    
    try:
        
        ip3=input("retype password\n")
        if ip3!=ip2:
            raise Exception
        else:
            print("login successful")
        break
        
    except:
        print("please enter correct password")

        counter+=1
        print("login failed")
        continue
    
