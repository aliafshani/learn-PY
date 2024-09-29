
def pass_checker(userPass):
    if len(userPass)< 8:
        print("your pass shouls be at least 8 Char ")
    elif userPass.isnumeric():
        print("your pass shuold have at list 1 string")
    elif userPass.isalpha():
        print("your pass shuold have at list 1 int")
    else:
        print("your pass is correct")
        
        
        
        
while True:
    userpass = input("enter pass : ")
    pass_checker(userpass)