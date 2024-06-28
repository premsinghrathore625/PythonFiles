class Student:
    def __init__(self,name,marks,height):
        print("adding a new student")
        self.name=name
        self.marks=marks
        self.height= height
        
s1=Student("krma",67,120)
print(s1.name,s1.marks,s1.height)        