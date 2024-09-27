myset = {"apple" , "mamme", "mooz" , "kiwi"}
myset2 = {"koon" , "mamme", "kos" , "kir"}

print("apple" in myset)
# >>> True

myset.add("kian")
print(myset)
# #############
# myset.update(myset2)
# print(myset)
# ###############
z = myset.intersection(myset2)
print(z)