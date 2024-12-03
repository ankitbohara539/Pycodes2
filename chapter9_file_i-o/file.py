
# # To read any created txt files in python with read() fn

# file = open('aboutme.txt','r')
# print (file.read())
# file.close()


# # Write to an existing file

# file = open("aboutme.txt",'a')
# file.write("I am a good boy, You knew that ?")
# file.close()


# # again we should open the appended file

# file = open ("aboutme.txt",'r')
# print(file.read())


# f = open("ankit.txt", 'a')
# f.write(" I am 20 years old young boy")
# f.close()

# f = open("ankit.txt", 'r')
# print(f.read())
 
# this is how we delete the created file in python

import os

os.remove('ankit.txt')
