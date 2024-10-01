# from moudel import hello , SMS
# from moudel import *

cs = [
    {
        "tittle" : "python",
        'teacher' : 'afshani',
    },{
        "tittle" : "js",
        'teacher' : 'milad',
    },{
        "tittle" : "php",
        'teacher' : 'nima',
    },
]


class User :   #parent
    def __init__(self , name , lastname):
        self.name = name
        self.lname = lastname
        
    def fullName(self):
        print(f'my full name is {self.name} {self.lname}')
        
        
        
class Student(User):   #child
    def __init__(self, name, lastname , email):
        super().__init__(name, lastname)
        self.email = email
        self.courses =[]
        
    def fullName(self):
        print("im a student")
        super().fullName()
        
    def printCourses(self):
        if self.courses:
            for course in self.courses:
                print(course["tittle"])
        else:
            print("you have no courses")





class Teacher(User):
    def __init__(self, name, lastname , code):
        super().__init__(name, lastname)
        self.code = code
        
    def fullName(self):
        print('im a teacher')
        super().fullName()
        
s1 = Student('ali' , 'afshani' , 'aliafshai@gmail.com')
s1.courses.append(cs[1])
s1.printCourses()