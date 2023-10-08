from fotrousiclass import Person
from fotrousiclass import Manager



per1 = Person("ali", "noori", 52, 123)
print(per1.f_name, per1.l_name, per1.ID, per1.age)
per1.info()

per2 = Manager("mahmoud", "zahmatkesh", 39, 543,"modir")
print(per2.f_name, per2.l_name, per2.ID, per2.age)
per2.info()
per2.sematt()