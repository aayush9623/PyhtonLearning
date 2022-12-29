class Student:
    # class/Static variable
    school = "Samra school"

    def __init__(self, m1, m2, m3):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method
    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3
    #accessors
    def get_m1(self):
        return self.m1
    #mutators
    def set_m1(self, value):
        self.m1 = value

    #class method
    @classmethod
    def school_info(cls):
        return cls.school

    #static method
    @staticmethod
    def info():
        print("This is student class")


s1 = Student(98, 78, 73)
s2 = Student(73, 45, 43)
print(s1.average())
print(s2.average())

print(Student.school_info())

Student.info()