class Person:
    def __init__(self, f_name, l_nsme, age, ID):

        self.f_name = f_name
        self.l_name = l_nsme
        self.age = age
        self.ID = ID

    def info(self):
        print("my info is :" +self.f_name+" "+self.l_name+ " "+str(self.age)+ " " +str(self.ID))
  #-------------------------------------------------------
class Manager(Person):
     def __init__(self,f_name,l_name,age,ID, semat):
        super().__init__(f_name,l_name,age,ID)
        self.semat = semat

     def sematt(self):
       print("my semat in fotrousi company is :"+self.semat)

     
        

           



        