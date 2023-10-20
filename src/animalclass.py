
class Animal:
    def __init__(self, esm, vazn, tol, arz):
        self.esm = esm
        self.vazn  = vazn
        self.tol = tol
        self.arz = arz
    def action(self):
        print("in jahate test action "+self.esm +" AST\n")


class Pestandaran(Animal):
    def __init__(self, esm, vazn, tol, arz, modeletavalod):
        super().__init__(esm, vazn, tol, arz)
        self.modeletavalod = modeletavalod
    def action2(self):
                 print("in jahate test22 action "+self.esm +" AST\n")
    def action3(self):
                 print("dar pestandaran modele tolid e mesl "+self.modeletavalod +" AST\n")       


class Khazandegan(Animal):
    def __init__(self, esm, vazn, tol, arz, modeletavalod):
        super().__init__(esm, vazn, tol, arz)
        self.modeletavalod = modeletavalod
    def action2(self):
                 print("in jahate test22 action "+self.esm +" AST\n")
    def action3(self):
                 print("dar "+ self.esm+ " modele tolid e mesl "+self.modeletavalod +" AST\n")       

        