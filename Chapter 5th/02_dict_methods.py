a = {
    "Perry": 100,
    "Phines": 89,
    "Ferb": 98,
    "Uwu": 1,
}

print(a.items())

a.popitem()
print(a)


a.pop("Perry")
print(a)


# print(a.items())
# print(a.update({"Perry":120, "Phines":99, "OwO":78}))
# print(a.keys())
# print(a.values())
#
# print(a)
# print(a.get("Perry"))
#
#
# difference between

# print(a["Perry"])
# print(a.get("Perry"))

# same output
# difference is in error outputs


print(a.get("Perry1"))  # givess none

# print(a["Perry1"]) #gives error
