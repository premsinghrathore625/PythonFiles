class HashTable:
    
    def __init__(self):
        self.max= 10
        self.arr=[[] for i in range (self.max)] 
        
    def hash(self,key):
        h=0
        for char in key:
            h+=ord(char) 
        return h % self.max
    
    def __getitem__(self,key) :
        h=self.hash(key)
        for kv in self.arr[h]:
            if (kv[0]==key):
                return kv[1]
    
    
    def __setitem__(self,key,val):
        h=self.hash(key)
        found=False
        for idx,element in enumerate(self.arr[h]) :
            if (len(element)==2 and element[0]==key):
                self.arr[h][idx]=(key,val)
                found=True
            if not found:
                self.arr[h].append((key,val))    
    
    
a=HashTable()
a["march 6"]=7
print(a["march 6"])
print(a.arr)
    
    
    