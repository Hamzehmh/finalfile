from fotrousiclass import Person
from fotrousiclass import Manager
from fotrousiclass import Karmand



per1 = Person("\nali", "Niazi", 52, 123)
print(per1.f_name, per1.l_name, per1.ID, per1.age)
per1.info()

per2 = Manager("\nAhmad", "Aghasiani", 39, 543,"modir")
print(per2.f_name, per2.l_name, per2.ID, per2.age)
per2.info()
per2.sematt()

per3 = Karmand("\nhasan", "kashani", 3923, 543,"khadamat")
print(per3.f_name, per3.l_name, per3.ID, per3.age)
per3.info()
per3.taskk()
#3#