# stored_pass = '12345'
# is_login = False



# while is_login == False :
#     userPassTest = input("enter your pass:")
#     if stored_pass == userPassTest :
#         print("welcome back dude")
#         is_login= True
#         break 
#     else:
#         print("go back to your home")

############################################################
users = {
    "ali":'12345',
    'mamad' : '2387',
    'farid' : "7800"
}

entres_username = input("enter your username:")
entres_pass = input("enter your pass:")

while entres_username not in users or entres_pass != users[entres_username]:
    print("your username or pass is wrong:")
    entres_username = input("enter your username:")
    entres_pass = input("enter your pass:")
    
print("you are logged in")
  