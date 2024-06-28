class HashTable:
    
    def __init__(self):
        self.max= 10
        self.arr=[None] * self.max
        
    def hash(self,key):
        h=0
        for char in key:
            h+=ord(char) 
        return h % self.max
    
    def __getitem__(self,key):
        h=self.hash(key)
        return self.arr[h]
    
    def __setitem__(self,key,val):
        h=self.hash(key)
        self.arr[h] = val
        
    def __delitem__(self,key) :
        h= self.hash(key)
        self.arr[h]=None
            
        
        
    
a=HashTable()

a["0"]=1
print(a["0"])     
print(a.hash("k"))    
print(ord("k"))
del a["0"]
print(a["0"])