class Cars:
    #class Variables stored in class namespace
    wheels = 4

    def __init__(self):
        #instance Variables stored in instance namespace
        self.mil = 10
        self.com = "BMW"



c1 = Cars()
c2 = Cars()
print(c1.com , c1.mil, c1.wheels)
print(c2.com , c2.mil, c2.wheels)
#changing the class variable by calling the class name
Cars.wheels=5
print(c1.com , c1.mil, c1.wheels)
print(c2.com , c2.mil, c2.wheels)
