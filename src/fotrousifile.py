from fotrousiclass import Person
from fotrousiclass import Manager
from fotrousiclass import Karmand
from fotrousiclass import Moshtari



per1 = Person("\nali", "Niazi", 52, 123)
print(per1.f_name, per1.l_name, per1.ID, per1.age)
per1.info()

per2 = Manager("\nAhmad", "Aghasiani", 39, 543,"modir")
print(per2.f_name, per2.l_name, per2.ID, per2.age)
per2.info()
per2.sematt()

per3 = Karmand("\nhasan", "kashani", 3923, 543,"khadamat\n")
print(per3.f_name, per3.l_name, per3.ID, per3.age)
per3.info()
per3.taskk()
#ajab roozeye

per4 = Karmand("\nhamid", "ahmadi", 44, 1443,"negahban\n")
print(per4.f_name, per4.l_name, per4.ID, per4.age)
per4.info()
per4.taskk()
#ajab roozeye emroooz va dirooooz

per5 = Moshtari("\nmoataaan", "haghiri", 44, 1443,"negahban"," lebese shab\n")
print(per5.f_name, per5.l_name, per5.ID, per5.age, per5.task, per5.)
per5.info()
per5.taskk()
per5.kharid()