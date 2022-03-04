
#just like that tried this code
"""lst=[1,2,'a','hello',3]
lst1=[]
for i in lst:
    try:
        i=10/i
        lst1.append(i)
        print(lst1)
    except:
        print("some error has occurred")"""

x=int(input("please enter number less than 10\n"))
try:
    if x>10:
        raise ValueError
except ValueError:
    print("please enter valid number")

else:
    print("entered right")
    
    

       
