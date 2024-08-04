file = open("first.txt")
data1 = file.read()
file2 = open("second.txt")
data2 = file2.read()
if data1==data2:
    print("The data is same in both the files.")
else:
    print("The content of both the files is not the same.")

file.close()
file2.close()

