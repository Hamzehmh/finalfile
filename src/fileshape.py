from classshape import Person
from classshape import Student


person1 = Person("ALi", "Rahmati", 42)
print(person1.f_name,person1.l_name, person1.age)
person1.info()
#=================================================

person2 = Student("Hasan", "gholami", 22)
print(person2.f_name, person2.l_name, person2.age)
person2.info()

