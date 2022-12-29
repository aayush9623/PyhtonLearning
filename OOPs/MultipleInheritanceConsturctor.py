class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("feature 1-A working")

    def feature2(self):
        print("feature 2 working")

#child class/sub class
#to inheritate the class do as below
class B():
    def __init__(self):
        print("In B init")

    def feature1(self):
        print("feature 1-B working")

    def feature4(self):
        print("feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")

    def feature5(self):
        print("feature 4 working")

    def feat(self):
        super().feature4()
        super().feature1()

#method resolution order will prefer the class inheritance from left to right
c1 = C()
c1.feature1()
c1.feat()

#output
#In A init
#In C init
#feature 1-A working


