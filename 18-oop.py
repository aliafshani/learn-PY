# class MyClass:
    
#     def __init__(self, name ,lastName):
#         self.myName = name
#         self.myLastname = lastName

# p1 = MyClass("alireza" , "ansari")
# p2 = MyClass("ahmad" , "movahedi")


# print(p1.myName , p1.myLastname)
# print(p2.myName , p2.myLastname)


##########################################################

# class Person :
#     def __init__(self , name , lastName , age) :
#         self.name = name
#         self.lastName = lastName
#         self.age = age
        
        
        
# person1 = Person('ali' , 'afshani' ,20)

# print(person1.name , person1.lastName , person1.age)


###########################################################

# class Person :
#     def __init__(self , name , lastName ) :
#         self.name = name
#         self.lastName = lastName
        
#     def fullName (self):    
#         print(f"hello from {self.name +" "+ self.lastName}")
        
        
# person1 = Person('ali' , 'afshani' )

# print(person1.name , person1.lastName )

# person1.fullName()

#############################################################################

class Person:
    def __init__(self,name , lastName , age):
        self.name = name
        self.lastname = lastName
        self.age = age

    def fullname(self):
        print(f'my name is {self.name} {self.lastname} and im {self.age}')


p1 = Person("ali" , "afshani" , 20)
p1.fullname()

p1.name = "kimia"
p1.fullname()