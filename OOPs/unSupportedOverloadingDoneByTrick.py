class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None :
            s=a+b
        else:
            s=a

        return s

s2 = Student(95, 25)
print(s2.sum(4,5,7))
print(s2.sum(4,5))