import re

# data = """555-555-5555
#           2346-134-1342
#           243-235-23455
#           242-235-2344"""
# restring = r"^(\d{3})(-)(\d{3})(-)(\d{4})$"
# matches = re.findall(restring, data, re.MULTILINE)
# print(matches)

# # date:
# print('name is salina')
# name= "salina"
# sur="mary"
# print("My name is ", name)
# print("My name is ",format(name))
# print(len(name))
# print(name[3:6])
# print(name[::-1])
# print (float(3/4))
# print(*name)
# print(name*3)
# print(name+"mary")
# print(name,sur,sep(->))
#!/bin/python3



if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 == 0):
        print ("n is even")
    elif 2<=n<=5:
        print(" Not Weird")
    elif 6<=n<=20:
        print("Weird")
    elif(n>20):
        print(" Not Weird")
    else:
        print("Weird")


