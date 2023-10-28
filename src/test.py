import random
from faker import Faker

fake = Faker()

fake.name()
print(fake)

for _ in range(10):
  print(fake.name())

tas1=random.randint(1,6)
tas2=random.randint(1,6)
tas3=random.randint(1,6)
print(tas1)
print(tas2)
print(tas3)

def test(a , b , c):
    return( a * b *c)
    """hello ooo45255

    Returns:
        _hello from the other side_
    """

x = test(tas1 , tas2 , tas3)
print(x)

class Joftshish:
    def __init__(self,tas11, tas22):
        self.tas11 = tas11
        self.tas22 = tas22

    def jofttshish(self):
        print("tas'haye man az in gharar ast"+ "-----"+ str(self.tas11)+" AND "+ str(self.tas22))
    def zarbjoftshish(self):
        return tas1 * tas2
        

x_1 = Joftshish(tas1 , tas2)        
x_1.jofttshish()
x_1.zarbjoftshish()

x_2 = Joftshish (8 , 12)
x_2.jofttshish()

#this is a frist commit for today0981
my_tuple = (1, 2, 2, 3)
print(my_tuple)

my_dic11 = {"a":1383 , "b": 20085}
print(my_dic11["b"])

my_list = ["kamal", "jamal", "mamal"]
print(my_list)

my_dic = {"a":4,"b":3, "c":9, "d":1}
print("my dic")
print(my_dic)

print(dict())
#with open(".src/test.txt") as book:
 #   print(book.read())0099


