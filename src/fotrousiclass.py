class Person:
    def __init__(self, f_name, l_name, age, ID):

        self.f_name = f_name
        self.l_name = l_name
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
#--------------------------------------------------------
class Karmand(Person):
     def __init__(self, f_name, l_name, age, ID, task):
        super().__init__(f_name, l_name, age, ID)
        self.task = task

     def taskk(self):
          print("my task in fotrousi company is :"+self.task)
#--------------------------------------------------------
class Moshtari(Manager):
     def __init__(self, f_name, l_name, age, ID, task, kharid):
        super().__init__(f_name, l_name, age, ID,ta)
        self.task = task
        self.kharid = kharid

     def taskk(self):
          print("my task in fotrousi company is :"+self.task)

     def kharid(self):
          print("my kharidddd in fotrousi company is :"+self.kharid)                
        
#avale sob e shanbe
#kheyli alli
#ye nafare jadid ezafe kardam be list e karmanda
     
        

           



        