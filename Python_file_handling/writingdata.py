# How to open a file
# Syntax-->f = open("filename","mode")
# e.g
f = open("abcd.txt","w")
#To close the file
f.close()



# #To write data in file...
# f=open("abc.txt","w") #Can't we modify the file name..
# f.write("rama\n")
# f.write("sachin\n")
# f.write("pintu\n")
#
# #To read data from file
# f = open("abc.txt","r")
# data = f.read()
# print(data)
#
# #To read first 10 charecters:
# f = open("abc.txt","r")
# data = f.read(10)
# print(data)  #rama sachi
#
#
# # to read data line by line
# # ================================
# f=open("abc.txt","r")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()


# to read all lines into list
# =========================
#f=open("abc.txt","r")
# lines=f.readlines()
# print(lines)
# for line in lines:
#     print(line)
# f.close()


#To read specific line by choice
#+==============================
f= open("abc.txt","r")
lines = f.readlines()
for line in lines():
    print(line(1))



