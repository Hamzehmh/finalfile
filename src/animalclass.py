
class Animal:
    def __init__(self, esm, vazn, tol, arz):
        self.esm = esm
        self.vazn  = vazn
        self.tol = tol
        self.arz = arz


    def action(self):
        print("in jahate test action "+self.esm +" AST")



class Pestandaran(Animal):
            def __init__(self, esm, vazn, tol, arz):

                super(Pestandaran, self).__init__(
                    esm=esm, vazn=vazn, tol=tol, arz=arz)


            def action2(self):
                 print("in jahate test22 action "+self.esm +" AST")


        