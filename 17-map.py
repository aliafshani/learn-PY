# myList = [2,5,67,78,6]

# def me(number):
#     return number * 2

# x = map(me , myList)
# print(list(x))

########################################

myList = [2,5,67,78,6]
myList2 = [78,2,657,38,4]

def me(number1 , number2):
    return number1 * number2

x = list(map(me , myList , myList2))
print(list(x))