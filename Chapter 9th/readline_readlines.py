# Reading lines
# file = open("read_lines.txt")
# data = file.readlines()
# print(data)
# file.close


#all come in a single list





# Reading line one by one
# file = open("read_lines.txt")
# data1 = file.readline()
# print(data1, type(data1))
# data2 = file.readline()
# print(data2, type(data2))
# data3 = file.readline()
# print(data3, type(data3))
# data4 = file.readline()
# print(data4, type(data4))
# data5 = file.readline()
# print(data5, type(data5))
# file.close()

#all are strings


# Shortcut
file = open("read_lines.txt")
data = file.readline()
while (data != ""):
    data = file.readline() #updating line number inside loop else it keeps pating the first line.
    print(data)
file.close()