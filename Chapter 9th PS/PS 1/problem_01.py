file = open("twinkle.txt")
data = file.read()
a = data.lower()
print(a)

if "twinkle" in a:
    print("Twinkle detected.")
else:
    print("Twinkle not detected")


file.close()
