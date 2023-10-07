class Shape:
   def __init__(self, color = "GRAY"):
      self.color = color



class Circle(Shape):
    def __init__(self, r, color = "RED") :
        self.color = color
        self.r = r

    def area(self,):
      return 3.14 * self.r * self.r   

    def mohit(self,):
      return 3.14 * self.r *2 