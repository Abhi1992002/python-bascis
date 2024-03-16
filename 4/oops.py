# object oriented programming -> we could use objects and classes for increasing reusability
# firstly create class -> it's like an blue print , we use this blue print to create an object (instance of a class)

class Student:
    name = "Abhimanyu"

s1 = Student()

print(s1.name)

print(type(Student))      #output <class 'type'>
print(type(s1))           #output <class '__main__.Student'>

# contructor -> _init_() , executed when a class is being initiated (means a object is created), if you do not write it , python make it and execute it

class Car:
    name1 = "car selector"       # here name1 is class attributes (common for all object instance)

    def __init__(self , name):   # self represent the object that is created
        self.name = name         # self.name is object attribute (unique of each object instance)
        print(self.name)
        self.name1 = name        # we could change class attributes
        print("hi ",self.name)

car1 = Car("tesla")
car2 = Car("cybertruck")

# methods -> function inside class 

class SmartPhone:
    category = "smartphone"

    def __init__(self,name):
        self.name = name

    # static method are used to create method which do not use self
    @staticmethod       # decorator -> use to wrap another function in order to extend the behaviour    
    def greeting():
        print("Hello , How are you")

    def hello(self):
        print(self.name , " category : " , self.category)    

smart1 = SmartPhone("i phone")
print(smart1.category)
smart1.greeting()
smart1.hello()

# There are 4 pillar of oops -> abstraction , encapsulation , inheritance , polymorphism

# abstraction -> hiding the implementation detail of a class and only show the essential feature to the user 
# example 

class Car:
    def __init__(self) -> None:
        self.acc = False
        self.brk = False
        self.clutch = False 
    
    def start(self):
        self.acc = True
        self.brk = True
        print("Car started.....")

c1 = Car()
c1.start()  # car class is not telling how it started a car , it hide the implementation details and only provide a feature to start the car 

# Encapsulation -> wrapping data and function in one unit (object), upto this point, whatever class we have created , we encapulate the data and method inside it 

# del keyword -> use to delete object or its attributes (not class attributes) 

del smart1.name
del smart1
print(s1.name)   # error

# Private(like) use to create attribute & method that can only be accessed inside the class 

class Account:
    __isPro = True                        # private class attribue
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass         # we can use 2 underscore in front of variable to make it private 

    def getAcc_no(self):
        print("account no : ",self.acc_no)

    def __getAcc_pass(self):              # private method
        print("Account password : ", self.__acc_pass )    

    def iam_verified_show_me_pass(self):
        self.__getAcc_pass()    


acc1 = Account("12345","password")   

# we can access acc_no 
print(acc1.acc_no)

# but can't acces acc_pass
# print(acc1.__acc_pass)         # error

acc1.iam_verified_show_me_pass()


## inheritance -> when one class derives the properties & methods of another class 

class Car:
    public_class_attribute = "public_class_attribute"
    __private_class_attribute = "private_class_attribute not inherited"
    def __init__(self,name) -> None:
        self.name = name
        self.acc = False
        self.only_in_car = "only present in Car class"
        self.brk = False
        self.clutch = False 
        self.__private = "it will not be inherited"
    
    def start(self):
        self.acc = True
        self.brk = True
        print("Car started.....")    

    def stop(self):
        self.acc = False
        self.brk = False
        print("Car stoped.....")  

class Car2:
    public_class_attribute = "public_class2_attribute"
    __private_class_attribute = "private_class_attribute not inherited"
    def __init__(self,name) -> None:
        self.name = name
        self.acc = False
        self.brk = False
        self.only_in_car2 = "only present in Car2 class"
        self.clutch = False 
        self.__private = "it will not be inherited"
    
    def start(self):
        self.acc = True
        self.brk = True
        print("Car2 started.....")    

    def stop(self):
        self.acc = False
        self.brk = False
        print("Car2 stoped.....")     

class teslaCar(Car2,Car):            # we give priority to class which inherited first , here car and car2 both have stop method , but my class we use car2 because it's come first     
    def __init__(self,name,prize) -> None:
        super().__init__(name)                   # super use to access methods of car2
        super().start()                          # but we can't access start because
        self.prize = prize

    def accessing_private_info_of_car(self):
        # print(self.__private)                      can't inherited
        print(self.public_class_attribute)    
        # print(self.__private_class_attribute)       can't inherited




car1 = teslaCar("tesla model s","1234")        

print(car1.name)
car1.start()
car1.accessing_private_info_of_car()

# class method -> another decorator
class Person(): 
    name = "Abhi"

    def changeObjName(self):
        self.name = "new_obj_name"        # it will only going to change for object not class

    def changeClassNameByNormalWay(self):
        self.__class__.name = "new_class_name"    # 1st method 
        Person.name = "new_class_name"            # 2nd method

    @classmethod
    def changeClassName(cls):
        cls.name = "new_name"                     # now the class attributer changed

p1 = Person()
p1.changeObjName()
print(p1.name)                                    # changed 
print(Person.name)                                # not changed 

p1.changeClassName()
print(p1.name)                                    # changed 
print(Person.name)                                # not changed 

# Property decorator -> used on a method to use it as a property 
# sometime we need to create an attribute which depends on another attribute and if change the another attribute , we need to change our attribute as well
# so we could use property method which can convert our method into attri
class Marks:
    def __init__(self,phy,chem,maths) -> None:
        self.phy = phy 
        self.chem = chem 
        self.maths = maths

    @property 
    def total(self):              # whatever it return, it coverts into attribute , we can access it using self.total
           return str(self.maths + self.maths + self.phy)


m = Marks(100,90,90)
print(m.total)

m.phy = 98
print(m.total)        # not changing after changing phy marks

# suppose we have created an attri named total and create an method which could change attri 
# but we need to manually change it like thiss 
# m.total 
# m.updateTotal()
# m.total              
# and with property we could create a method which can be used as attribute (and update automatically)


# @getter and @setter -> also decorators 

# Polymorphism -> polymorphism in programming is a concept that allows you to perform a single action in different ways depending on the type of object.
# example -> operator overloading 
# when the same operator is allowed to have different meaning acc to context 

print(1+2)                    # here + uses to add
print("hello"+"how")          # concantenation
print([1,2]+[3,4])            # merge 

# here for adding / merge / concat , we are using dunder function -> + = __add__
# a+b -> a.__add__.(b) , inbuilt in python 
# write now + dunder does'not support to add 2 complex number , but we make out class to use + to add 2 complex number
# if we use __add__ dunder function in our class so we can now know how to add 2 objects of this class

class Complex():
    def __init__(self,real,img) -> None:
        self.real = real
        self.img = img 

    def showNumber(self):
        print(str(self.real) + "i " + " + "  + str(self.img) + "j ")  

    def __add__(self,num2):
        real = self.real + num2.real
        img = self.img + num2.img    
        return str(real) + "i " + " + "  + str(img) + "j "

num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(3,4)
num2.showNumber()

num3 = num1 + num2    # it means num1.__add__(num2) , here num is obj and i am passing a second num2 object to its method name __add__
print(num3)