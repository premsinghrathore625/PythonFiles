class Person:
    name="anonymus"
    
    @classmethod
    def changename(cls,name) :
        cls.name=name 
        
p1=Person()
p1.changename("rahul")
print(p1.name)
print(Person.name)        
        