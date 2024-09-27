# thisList = ["apple" , "banana" , "cherry",True]
# print(thisList[0:])

# ###########################################################

# doost = ["ali" , "mamad" , "fatemeh" , "avina"]
# print(doost[:3])
# print(doost[2:])
# ############################################################
# doost = ["ali" , "mamad" , "fatemeh" , "avina"]
# print(doost)
# doost[0:]= ["nini" , " nini" , "momo" , "kio"]
# print(doost)
# doost = ["ali" , "mamad" , "fatemeh" , "avina"]
# doost[1:4] =[ "momomo"]
# print(doost)
# doost.insert(3 , "kian")
# print(doost)
# ###############################################################
doost = ["ali" , "mamad" , "fatemeh" , "avina"]
# doost.remove("mamad")
# doost.sort()
# print(doost)
# ##############################################################
enemy = doost.copy()
list3 = enemy + doost
list3.sort()
print(list3)