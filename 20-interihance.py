class Person:
    def __init__(self , name , lastName):
        self.name = name
        self.lastname = lastName



        
class Student(Person):
    def __init__(self, name, lastName , age):
        super().__init__( name , lastName)
        self.age = age
        
S1 = Student('ali' , 'afshani' ,29)