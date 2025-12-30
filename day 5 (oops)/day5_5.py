# problem solving 

# create a product store in which price aand name of the product is stored.

class product:
    def __init__(self,name, price):
        self.name=name
        self.price=price

    def get_info(self):
        print(f"price is {self.price} for the {self.name}")

p1=product("phone", 15000)
p2=product("tablet", 20000)
p3=product("laptop",50000)
p4=product("pen", 10)
 
p1.get_info()
print("name of the product-3 is: ",p3.name)
