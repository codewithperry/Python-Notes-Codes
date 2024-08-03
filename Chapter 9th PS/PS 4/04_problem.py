openfile = open("PS 4/abuse.txt", "r")
data = openfile.read()
uwu = open("PS 4/abuse.txt", "w")

replacer = data.replace("donkey", "###")
uwu.write(replacer)