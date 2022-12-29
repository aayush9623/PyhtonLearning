class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # first way of creating object of innner class
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    # inner class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.ram, self.cpu)


s1 = Student("Aayush", 45)
s2 = Student("Nirnay", 44)
s1.show()
s2.show()
#lap1 = s1.lap
#lap2 = s2.lap
#lap1.show()
#lap2.show()

#s1.show()
#print(s1.lap.brand)
# You can create object of inner class inside the outer class or
# you can create object of inner class outside the outer class provided you use outer class name to call it
#lap = Student.Laptop()
#lap.show()
