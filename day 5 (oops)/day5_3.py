# methods
# instance , class, static

# instance ( can access class attributes as well as instance attributes)

class laptop:
    storage_type="ssd" # class attribute (generally those info which is common to all)

    def __init__(self, ram, storage):
        self.ram=ram
        self.storage=storage
    
    def get_info(self):
        print(f"laptop has{self.ram} RAM and {self.storage} {self.storage_type} ") 

l1= laptop ("16gb", "512gb")
l2= laptop ("8gb", "512gb")
print(l1.ram)
print(laptop.storage_type)
l1.get_info()


