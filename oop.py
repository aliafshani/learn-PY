class MyClass:
    
    def __init__(self, name ,lastName):
        self.myName = name
        self.myLastname = lastName

p1 = MyClass("alireza" , "ansari")
p2 = MyClass("ahmad" , "movahedi")


print(p1.myName , p1.myLastname)
print(p2.myName , p2.myLastname)