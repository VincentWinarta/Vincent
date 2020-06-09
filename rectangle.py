class rectangle:
    def __init__(self, length=0, width=0):
        self.length=length
        self.width=width

    def input1(self):
        panjang=int(input("Insert length :"))
        lebar=int(input("Insert width :"))
        self.length=panjang
        self.width=lebar
     
    
    #method
    def run(self):
        area=self.length*self.width
        return area

rectangle1=rectangle()
area_rectangle1=rectangle1.run()

print("Area : ", area_rectangle1)
ask=rectangle1.input1()

area_rectangle1=rectangle1.run()

print("Area : ", area_rectangle1)