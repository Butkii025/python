# class  attriibute methode;
# static attribute methode;


class laptop:
    storage_type="ssd" # class attribute (generally those info which is common to all)

    def __init__(self, ram, storage):
        self.ram=ram
        self.storage=storage


    @classmethod  # changes the behaviouur of methode to "Class"

    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    @staticmethod  # static methods

    def calcualate_discount(price, discount):
        final_price=price-(discount*price/100)
        print(final_price)

l1= laptop ("16gb", "512gb")
l2= laptop ("8gb", "512gb")
print (l1.ram)
l1.get_storage_type()

l1.calcualate_discount(400000,10)


