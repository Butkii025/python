# encapsulation :: wrapping data and function in single unit  ~~ 💊

class Bank_account:
    def __init__(self, name, balance):
        self.name=name  # public
        #self._balance = balance  # protrotected using single underscore " _ " 

        self.__balance=balance  # it`s private and can not be accessed easily

    """and if we use doule underscore " __ ", 
    then it will become more protected and can not access by normal Class we have to create (getter & setter) 
    for accessing the prive information"""

    def get_balance(self):  # using getter
        return self.__balance
    
    
    def set_balance(self,newBalance):  # using setter for setting new amount
        self.__balance = newBalance
    
acc1=Bank_account("rahul", 100)
acc1.set_balance(50)

print(acc1.name, acc1.get_balance())

