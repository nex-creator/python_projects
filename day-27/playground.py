def add(*args):
    sum = 0
    for num in args:
        sum +=num
    return sum
print(add(3,5,6,9,90))

def calculate(n,**kwargs):
    n +=kwargs["add"]
    n *=kwargs["multiply"]
    print(n)




calculate(2,add =3, multiply =5)

class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw.get("model") # using get() we can return none if not intiallized

my_car =  Car(make = "Nissan")
print(my_car.model)