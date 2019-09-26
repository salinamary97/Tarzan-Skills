# 1 :  finding sum of num through call function

def sum_of_numbers(num1, num2):
    result= num1 + num2
    return result
print(sum_of_numbers(5,3))

# 1 :  finding odd or even num through call function

def check(n):
    if n%2==0:
        print ('even')
    else:
        print('odd')
    return n

check(5)
check(2)

# factorial of num

n= int(input("enter the number : "))
def fact(n):
    if n==0:
        return 1
    else:
        X = n*fact(n-1)
        return X
print(fact(n))

# print details using call function

def greet1( name, msg="Good Morning"):
    print(f"hi {name} {msg}")
greet1("salina")
#
def greet(*names):
    for name in names:
        print(f"hi {name}")
greet("salina", "sagar", "sangeetha")

# * asterisk function

def sum_(*args):
    return sum(args)
print(sum_(2, 2, 2, 2 ,2))

def fruits(**kwargs):
    if 'fruit' and 'cars' in kwargs:
        print(f'{kwargs["fruit"]}, {kwargs["cars"]}')
fruits(fruit= 'apple', cars= 'BMW')







