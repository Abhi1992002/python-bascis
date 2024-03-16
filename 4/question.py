# create a student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average 

class Student:
    def __init__(self,name,):
        self.name = name

    def findAverage(self,marks):
        sum=0
        for el in marks:
            sum += el 
        print("average : " , sum/3)
        
    
s1 = Student("abhimanyu") 
s1.findAverage([50,40,30])

# create account class with 2 attributes - balance & account no. and also create methods and credits& printing the balance 

class Account:
    def __init__(self,acc,balance) -> None:
        self.acc = acc
        self.balance = balance

    def credit(self,amount):
        self.balance += amount
        print("amount credited successfully")
        
    def debit(self,amount):
        self.balance -= amount
        print("amount debited successfully")

    def checkBalance(self):
        print("Your current balance is : ",self.balance)    

acc1 = Account(12345,1000)
acc1.credit(500)
acc1.checkBalance()        
acc1.debit(300)
acc1.checkBalance()

## Create a class called Order which stores items & its price.
# Use Dunder function __gt__() to convey that: 
# order1 > order2 if price of order1 > price of order2 

class Order:
    def __init__(self,price,item) -> None:
        self.price = price 
        self.item = item 

    def __gt__(self,num2):
        if(self.price > num2.price):
            print("true")
            return True 
        else:
            print("false")
            return False 

o1 = Order(500,"I Phone")            
o2 = Order(300,"Nothing 2A")

o1>o2       
o2>o1