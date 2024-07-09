s = set()
s.add(20)
s.add(20.0)
s.add("20")  # lenth of s after these operations
print(s)
print(len(s))
#surprisingly ans is 2! not 3 uwu
print(1 == 1.0) #they are same in python lol