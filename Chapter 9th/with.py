# Using with statements to avoid writing f.close() againt and again
with open("with.txt") as file:
    data = file.read
    print(data)
#f.close no need as it will be automatically
# doneby with statements

