# def is_big_little(name =""):
#     little = 0
#     big = 0
#     for i in name:
#         if i.islower():
#             little += 1
#         else:
#             big +=1
#     print (f'your name has {little} lower case')
#     print (f'your name has {big} bigger case')


# is_big_little("AlireZA")

################################################################
# def is_odd(number = 5):
#     if number % 2 ==1:
#         print("fard")
#     else:
#         print("zoj")
    
    
# while True:
#     number = int(input("enter your number : "))
#     is_odd(number)

##################################################################################
date_of_date = int(input("enter your date bitrth"))
date_of_mounth = int(input("enter your mounth bitrth"))
date_of_year = int(input("enter your year bitrth"))

def birthCalculatore(day ,mounth , year):
    if day>10  >= 10 and  mounth:
        year +=622
    else:
        year += 621
        
    print(f"you birth in {year}")

birthCalculatore(date_of_date , date_of_mounth , date_of_year)