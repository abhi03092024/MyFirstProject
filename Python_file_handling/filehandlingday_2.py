"""
# f = open("abc.txt","w")
# f.write("Abhaya \n")
# f.write("KAnha \n")
# f.write("Biswa")
#


#To remove file data
# with open("abc.txt",'w') as file:
#     file.write("")
#
# remove or replace specific data

#-------------------------------
with open("abc.txt","r") as file:
	data = file.read()
modified_data = data.replace("abhaya", "biswa1")
with open("abc.txt",'w') as file:
	file.write(modified_data)
## Note-->Once we perform the replace method we must have to write the data in the file to see the changes


filename = 'abc.txt'
content_to_remove = 'biswa1'
remove_specific_content=(filename, content_to_remove)

# remove the specified line
# -------------------------
with open("abc.txt", "r") as file:
	lines = file.readlines()

if 1 <= 1 <= len(lines):
	del lines[1 - 1]

with open("abc.txt", 'w') as file:
	file.writelines(lines)
"""
# write into specific line
# == == == == == == == == == == == == == == ==
with open("abc.txt", 'r') as file:
    lines = file.readlines()

if 1 <= 2 <= len(lines):
    lines[2 - 1] = "sachin" + '\n'

with open("abc.txt", 'w') as file:
    file.writelines(lines)











