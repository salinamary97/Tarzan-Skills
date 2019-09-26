First_Name = str(input("Enter your First Name : "))
Last_Name = str(input("Enter your Last Name : "))
Name = str(First_Name + Last_Name)
print("your Name is : ", Name)
X= Name[::-1]
print("resverse of your Name: ",X)

def Grocery(*veggies):
    for Grocery_ in veggies:
        print(Grocery_)
Grocery('Tomato','potato','carrot','beans')
