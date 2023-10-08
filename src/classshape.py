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
        print("my text is:" +self.f_name)
        