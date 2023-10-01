from classtest import car
from classtest import Motor

car_1 = car("pride", "131", 2023, "blue")
car_2 = car("benz", "c200", 2022, "RED")

#print(car_1.model)
#print(car_1.year)
#print(car_1.color)
#print(car_1.make)



print(car_1.make,car_1.model, car_1.color, car_1.year)
print(car_2.make,car_2.model, car_2.color, car_2.year)

car_2.drive()
car_1.stop()
#----------------------------------------------------------
Motor_1 = Motor("yamaha", "RS", "Red", 1985)
Motor_2 = Motor("Honda", "XL", "yellow", 2002)

print(Motor_1.model, Motor_1.brand, Motor_1.color, Motor_1.year)

Motor_1.max()
Motor_1.cc()

print(Motor_2.model, Motor_2.brand, Motor_2.color, Motor_2.year)

Motor_2.max()
Motor_2.cc()


