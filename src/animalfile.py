from animalclass import Animal
from animalclass import Pestandaran
from animalclass import Khazandegan



animal_1 = Animal("Khar", 125, 250, 140)
print(animal_1.esm, animal_1.vazn, animal_1.tol, animal_1.arz)
animal_1.action()



animal_2 = Pestandaran("asb", 125, 250, 140,"zayeman")
print(animal_2.esm, animal_2.vazn, animal_2.tol, animal_2.arz, animal_2.modeletavalod)
animal_2.action3()
animal_2.action()

animal_3 = Khazandegan("Temsaah", 355, 450, 90,"Tokhmgozar")
print(animal_3.esm, animal_3.vazn, animal_3.tol, animal_3.arz, animal_3.modeletavalod)
animal_3.action3()
animal_3.action()