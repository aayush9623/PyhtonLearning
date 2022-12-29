class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

#child class/sub class
#to inheritate the class do as below
class B():
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A,B):
    def feature5(self):
        print("feature 4 working")


c1 = C()
c1.feature1()

b1= B()
b1.feature4()