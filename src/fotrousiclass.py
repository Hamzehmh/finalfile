class Person:
    def __init__(self, f_name:str, l_name:str, age:int, ID:int):
         """_salam az khone_

         Arguments:
             f_name -- _frist name _
             l_name -- _last namee_
             age -- _years old of persono
             ID -- _ID numberr_
         """
         self.f_name = f_name
         self.l_name = l_name
         self.age = age
         self.ID = ID

    def info(self):
        print("my info is :" +self.f_name+" "+self.l_name+ " "+str(self.age)+ " " +str(self.ID))
  #----------------------------------------------------------------------
class Manager(Person):
     def __init__(self,f_name,l_name,age,ID, semat):
        super().__init__(f_name,l_name,age,ID)
        self.semat = semat

     def sematt(self):
       print("my semat in fotrousi company is :"+self.semat)
#-----------------------------------------------------------------------
class Karmand(Person):
     def __init__(self, f_name, l_name, age, ID, task):
        super().__init__(f_name, l_name, age, ID)
        super().info()
        self.task = task

     def taskk(self):
          print("my task in fotrousi company is :"+self.task)

#-----------------------------------------------------------------------
class Moshtari(Manager):
     def __init__(self, f_name, l_name, age, ID, semat, kharid):
        super().__init__(f_name, l_name, age, ID,semat)
        self.kharid = kharid

     def semat2(self):
          print("my task in fotrousi company is :"+self.semat)

     def kharid2(self):
          print("my kharidddd in fotrousi company is :"+self.kharid)    


        

     
        

           



        