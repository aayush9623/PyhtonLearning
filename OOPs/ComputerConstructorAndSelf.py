class Computer:
    def __init__(self):
        self.name = "Aayush"
        self.age = 24

    def update(self):
        self.age=30

    def compare(self,other):
        if self.age==other.age:
            return True
        return False

c1 = Computer()
c2 = Computer()
#print(id(c1))
#print(id(c2))
print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

c1.update()
c2.name= "Rushi"
print(c2.name)
print(c1.age)
print(c2.age)
if c1.compare(c2):
    print("They are same ")
else:
    print("They are not same")