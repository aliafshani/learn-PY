names1 = ["amir" , 'amin' , 'ali' , 'ahmad' , 'reza' , 'akbar' , 'mehdi' , 'milad'] 
names2 = ["mostafa" , 'amin' , 'kian' , 'nima' , 'jina' , 'akbar' , 'mimi' , 'kir'] 

empty_list = []

for name1 in names1:
    for name2 in names2:
        if name1 == name2:
            empty_list.append(name1)
print(empty_list)