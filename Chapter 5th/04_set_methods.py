o = {1, 33, 23, 213, 6243, 21312452362}
o2 = {1, 23, 43, 654, 41234, 341515125}

i1 = {1, 11, 111, 1111}
i2 = {1, 12, 112, 1111, 11112}

# len only count one set lenth at once
# print("Lenth of the sets used in this file are:",len(o, o2, i1, i2))
print("Lenth of the set o is:", len(o))
print("Union of o and o2", o.union(o2))
print("Intersection of i1 and i2", i1.intersection(i2))


o.add("Perry")
print("Added Perry to set o:", o)

o.remove(1)
print("Removed 1 from set o:", o)

o.pop()
print("Popped a random element:", o)
