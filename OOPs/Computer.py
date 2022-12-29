class Computer:
    #its like a constructor called as init method which automatically call when object is created
    def __init__(self,  CPU,  Ram):
        self.cpu = CPU
        self.ram = Ram

    def config(self):
        print("config is : ", self.cpu , self.ram)

comp1 = Computer("i5","16Gb")
comp2 = Computer("Ryzen","16Gb")

comp1.config()
comp2.config()
#Computer.config(comp1)