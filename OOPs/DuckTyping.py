class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("convention check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()


ide =pycharm()

ide1 = MyEditor()
lap1 =Laptop()
lap1.code(ide)
print()
lap1.code(ide1)