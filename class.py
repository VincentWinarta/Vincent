class Flower :
    def __init__(self,name,petals,price):
        self.name = str(name)
        self.petals = int(petals)
        self.price = float(price)
    
    def discount(self):
        self.price*=0.8
        return self.price
    
    def introduce(self):
        return f'This is {self.name} with {self.petals} petals'

flower1=Flower("Mawar",4,5.6)
flower2=Flower("Melati",5,6.7)

discount_flower1=flower1.discount()
discount_flower2=flower2.discount()
run=flower1.introduce()
print(run)
print("Price :" ,flower1.price)


