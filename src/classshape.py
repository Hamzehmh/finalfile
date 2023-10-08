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
class moraba(Regtangle):
   def __init__(self, zel, color="green"):
      super().__init__(tol, arz, color)
      self.zel = tol  
      
      self.arz = zel