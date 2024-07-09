a = {
    "Aalu": "Potato",
    "Aangur": "Grapes",
}
print(type(a))

b = input("Enter what word you want to loockup for?:")
c = a.get(b)
print(c)
