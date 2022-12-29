class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

#child class/sub class
#to inheritate the class do as below
class B(A):
    def __init__(self):
        super().__init__()
        print("In B init")

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


b1=B()
