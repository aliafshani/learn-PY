# names1 = ["amir" , 'amin' , 'ali' , 'ahmad' , 'reza' , 'akbar' , 'mehdi' , 'milad'] 
# names2 = ["mostafa" , 'amin' , 'kian' , 'nima' , 'jina' , 'akbar' , 'mimi' , 'kir'] 

# empty_list = []

# for name1 in names1:
#     for name2 in names2:
#         if name1 == name2:
#             empty_list.append(name1)
# print(empty_list)


# ###################################################################

name = input("enter your name : ")
name = name.lower()
name = name.replace(" " ,"")
b =[]


for item in name:
    if item not in b:
        print(f'your name has {name.count(item)}  {item}')
        b.append(item)