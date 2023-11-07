from math import sqrt

class Vector:
    def __init__(self,arr):
        self.arr=arr
        self.len=len(self.arr)
    
    def add(self,b):
        if self.len != b.len:
            raise ValueError
        temp=Vector([])
        for i in range(self.len):
            temp.arr.append(self.arr[i]+b.arr[i])
            temp.len+=1
        return temp
    
    def subtract(self,b):
        if self.len != b.len:
            raise ValueError
        temp=Vector([])
        for i in range(self.len):
            temp.arr.append(self.arr[i]-b.arr[i])
            temp.len+=1
        return temp
    
    def dot(self,b):
        if self.len != b.len:
            raise ValueError
        sum=0
        for i in range(self.len):
            sum+=self.arr[i]*b.arr[i]
        return sum
    
    def norm(self):
        sum=0
        for i in range(self.len):
            sum+=self.arr[i]**2
        return sqrt(sum)
    
    def equals(self,b):
        if self.len != b.len:
            return False
        for i in range(self.len):
            if self.arr[i] != b.arr[i]:
                return False
        return True
    
    def __str__(self):
        Str='('
        for x in self.arr:
            Str=Str+str(x);
            if x!=self.arr[-1]:
                Str=Str+','
        Str=Str+')'
        return Str;