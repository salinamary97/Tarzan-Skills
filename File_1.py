# File close automatically
#
# with open("salina.txt","r") as file:
#     print(file.readline())
#
# # File with close statement
#
# file_1 = open("salina.txt","r")
# print(file_1.read())
# file_1.close()
#
# # Example of a file
#
# with open("salina.txt","r") as file:
#      content= file.readlines()
#      for line in content:
#         print(line, end='')

#Example 2 of a read file function

# with open("salina.txt","r") as file:
#     content = file.readline()
#     print(content, end="")
#     content = file.readline()
#     print(content, end="")
#     content = file.readline()
#     print(content, end="")
#     content = file.readline()
#     print(content, end="")
#     content = file.readline()
#     print(content, end="")
#     content = file.readline()
#     print(content, end="")

# Example 3 :
#
# with open("salina.txt","r") as file:
#     for line in file:
#         print(line, end=" ")

# Example 4 :

# with open("salina.txt","r") as file:
#     content = file.read(3)
#     print(content)

# Example 5:

#
# with open("salina.txt","r") as file:
#     content = file.read(3)
#     print(content)
#     content = file.read(3)
#     print(content)
#     content = file.read(3)
#     print(content)

# Example 6 :
#
# with open("salina.txt","r") as file:
#     print(file.read(10))
#     print(file.readlines(10))
#     file.seek(10,0)
#     print(file.read(10))

# Example 7 :

# with open("Varun.txt","w") as file1:
#     file1.write("Test")
#     file1.seek(0)
#     file1.write('R')

# Example 8 : Copy a jpeg file

# with open("Desktop-Computers.jpg","rb") as rf:
#     with open("rf.jpg", "wb") as wf:
#         for line in rf:
#             wf.write(line)

# Example 9 :

with open("Desktop-Computers.jpg","rb") as rf:
    with open("image_comp.jpg", "wb") as wf:
        chunk_Size = 7829797079
        rf_chunk = rf.read(chunk_Size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_Size)



