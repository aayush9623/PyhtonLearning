class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = m1 + m2
        return s3

    def __gt__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        if m1 > m2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(59, 46)
s2 = Student(95, 25)
#Its Comment
#Below is documentation
"""
 in background Student.__add__(s1,s2)
demo
"""
s3 = s1 + s2

print(s3)


a = 9
print(a)
#in background  print(a.__str__())

print(s1.__str__())