with open("rename.txt") as f:
    data = f.read()
with open("renamed_by_python.txt", "w") as write:
    write.write(data)
