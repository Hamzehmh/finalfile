from src.fotrousiclass import Person as pe
from fotrousiclass import Manager
from fotrousiclass import Karmand
from fotrousiclass import Moshtari

#this is a frist commit for todaydg 9865

per1 = pe("\nali", "Niazi", 52, 123)
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
#gfgh

per4 = Karmand("\nhamid", "ahmadi", 44, 1443,"negahban\n")
print(per4.f_name, per4.l_name, per4.ID, per4.age)
per4.info()
per4.taskk()


per5 = Moshtari("\nmosataaan", "haghiri", 84, 13,"negahban"," lebese shab")
print(per5.f_name, per5.l_name, per5.ID, per5.age, per5.semat, per5.kharid)
per5.info()
per5.semat2()
per5.kharid2()


per6 = Moshtari("\nyaser", "zarjooo", 41, 145,"operatoor"," shorte varzeshi")
print(per6.f_name, per6.l_name, per6.ID, per6.age, per6.semat, per6.kharid)
per6.info()
per6.semat2()
per6.kharid2()


 