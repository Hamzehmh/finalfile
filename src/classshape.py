<<<<<<< HEAD
class Shape:
   
   def __init__(self, color = "GRAY"):
      self.color = color

#------------------------------------------------------------------

class Circle(Shape):
  """this is a Circle class-is my exersize

  Arguments:
      Shape --this is my frist test
  """

  def __init__(self, r, color = "rrr"):
        super().__init__(color)
        self.r = r

  def area(self,):
      return 3.14 * self.r * self.r   
    
  def mohit(self,):
      return 3.14 * self.r *2 
#------------------------------------------------------------------------------    
    
class Regtangle(Shape):
    def __init__(self, tol, arz, color="green"):
        super().__init__(color)
        self.tol = tol
        self.arz = arz

    def area(self,):
      return self.tol * self.arz
        
    def mohit(self,):
      return 2*self.tol + 2* self.arz
    #---------------------------------------------------------------------------------
        
=======
class Person:
   
     def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

     def info(self):
        print("My info is : "+self.f_name+" "+self.l_name)

#=====================================================================
class Student(Person):
    
    def info(self):
        print("my text is:" +self.f_name+" "+self.l_name)
#=====================================================================
class Teacher(Person):
    
    def info(self):
        print("my Teacher is:" +self.f_name+" "+self.l_name)        
>>>>>>> f974980e6e1eb0ee7852da64812b518c0e15e592
