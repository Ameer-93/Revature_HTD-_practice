#abstract

'''from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class bike(vehicle):
    def start(self):
        print("bike started")

b=bike()
b.start()'''

#inheritance

'''class bike:
    def show(self):
        print("bike is looking good")
class car(bike):
    def start(slelf):
        print("car has self")
c=car()
c.show()
c.start() '''    

#types of inheritance

#single inheritance

'''class dog:
    def bark(self):
        print("barking")
class cat(dog):
    def show(self):
        print("showing")
c=cat()
c.bark()
c.show()'''


#multiple inheritance

'''class dog:
    def bark(self):
        print("barking")
class cat(dog):
    def bal(self):
        print("balance")
class bird(dog,cat):
    def show(self):
        pass
        #print("showing")
b=bird()
b.bark()  '''

#multilevel inheritance

'''class cat:
    def show(self):
        print("baeking")
class dog(cat):
    def show(self):
        print("showing")
class penguin(dog):
    def show(self):
        print("penguin cannot fly")
p = penguin()
p.show() '''


#Herichical inheritance

'''class cat:
    def show(self):
        print("cat cannot fly")
class dog(cat):
    def show(self):
        print("dog is not fly")
class hero(cat):
    def show(self):
        print("hero is good")
h=hero()
h.show() '''


#Hybrid inheritance

class cat:
    def show(self):
        print("barking")
class dog(cat):
    def show(self):
        print("penguin")
class penguin:
    def show(self):
        print("printing")
class bike(dog,penguin):
    def show(self):
        print("watering")

b=bike()
b.show()                    
            



#ploymorphism

'''class bird:
    def fly(slef):
        print("bird can fly")
class penguin(bird):
    def fly(self):
        print("penguin cannot fly")
def flying_test(bird):
        bird.fly()
b1=bird()
b2=penguin()
flying_test(b1)
flying_test(b2)'''

#encapsulation

'''class Account:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance +=amount
    def get_balance(self):
        return self._balance
acc = Account(100)
acc.deposit(500)
print(acc.get_balance)'''

'''class Public:
    def __init__(self):
        self.name = "John"  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
#print(obj.name)  # Accessible'''


          




        