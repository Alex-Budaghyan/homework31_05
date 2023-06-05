cars = 100  # the number of cars
space_in_a_car = 4.0  # the space occupying by each car
drivers = 30  # the number of drivers
passengers = 90  # the number of passengers
cars_not_driven = cars - drivers  # the number of cars that have not a driver
cars_driven = drivers  # the number of cars that have a driver
carpool_capacity = cars_driven * space_in_a_car  # the space occupying by all cars
average_passengers_per_car = passengers / cars_driven  # the average number of passengers per each car
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# 1.carpool_capacity will be equal 120 because it is the production of two int numbers

# 6.    python3
#       i = 9
#       x = 5
#       y = 6
#       i + x * y
