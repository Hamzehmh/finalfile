from classtest import car

car_1 = car("pride", "131", 2023, "blue")
car_2 = car("benz", "c200", 2022, "RED")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)



print(car_1.make,car_1.model, car_1.color, car_1.year)
print(car_2.make,car_2.model, car_2.color, car_2.year)

car_2.drive()
car_1.stop()

print("Hello from my rook in gilavand")   