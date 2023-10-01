class car:

 def __init__(self, make, model, year, color):
     self.make = make
     self.model = model
     self.year = year
     self.color = color

 def drive(self):
    print("this " +self.make + "  is driving")


 def stop(self):
    print("this " +self.make + " is stoped")


 
       

class Motor:

   def __init__(self, brand, model, color, year):

    self.brand = brand
    self.model = model
    self.color = color
    self.year = year
   

   def max(self):
       print("max speed this moter " +self.brand + " is max ")

   def cc(self):
        print("max CC this moter "+self.brand + " is very CCCC ")
      




