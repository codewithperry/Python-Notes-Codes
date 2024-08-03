openfile = open("PS 5/abuse.txt", "r")
data = openfile.read()


abuse_list = ["ls", "bc", "mc"]
for word in abuse_list:
    uwu = open("PS 5/abuse.txt", "w")
    replacer = data.replace(word, "###")
    uwu.write(replacer)


uwu.close()
openfile.close()
