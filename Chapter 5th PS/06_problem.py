fav_lang = {}
# print(type(fav_lang))
a = input("Enter your name:")
e = input("Enter your fav lang:")

b = input("Enter your name:")
f = input("Enter your fav lang:")

c = input("Enter your name:")
g = input("Enter your fav lang:")

d = input("Enter your name:")
h = input("Enter your fav lang:")


fav_lang[a] = e
fav_lang[b] = f
fav_lang[c] = g
fav_lang[d] = h


print(fav_lang)
print(type(fav_lang))


# other way
# name = input("Enter your name:")
# lang = input("Enter your fav lang:")
# fav_lang.update(name: lang)
# print(fav_lang)
# name every time after input
# but if 2 people name are same then the latest one will be considered as the real fav lang. as it is auto updating through update function.
# but if name is different in this and language is same no problem it will be ok as identifier is always key not valueee.

