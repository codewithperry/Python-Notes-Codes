# dont use 0 in starting of anything in dictonary
# how to create empty dict?
empty_dict = {}
marks = {
    "Perry": 100,
    "Moo": 100,
    "Git": 90,
    "dic": 120,
    10: "Abdul",
}
print(type(marks))
print(len(marks))
print(marks)
print(type(marks))
print(type("Moo"))
print(marks["Perry"])
print(marks["Moo"])


# trying again

result = {
    "Perry": 100,
    "Shubham": 90,
    "Shreya": 10,
    0: "Ayan",
}

print(result, type(result))
print(result["Perry"])
# print(result["Ayan"]) #error
print(result[0])
