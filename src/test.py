import random
tas1=random.randint(1,6)
tas2=random.randint(1,6)
tas3=random.randint(1,6)
print(tas1)
print(tas2)
print(tas3)

def test(a , b , c):
    return( a * b *c)
    """ahsant be shoma
    """

x = test(tas1 , tas2 , tas3)
print(x)

class Joftshish:
    def __init__(self,tas11, tas22):
        self.tas11 = tas11
        self.tas22 = tas22

    def jofttshish(self):
        print("tashaye man az in gharar ast"+ "-----"+ str(self.tas11)+" AND "+ str(self.tas22))
    def zarbjoftshish(self):
        return tas1 * tas2
        

x_1 = Joftshish(tas1 , tas2)        
x_1.jofttshish()
x_1.zarbjoftshish()


