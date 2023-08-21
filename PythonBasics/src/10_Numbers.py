demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

print(39 - 16)
print(abs(16 - 39)) #Absoulte

print(round(14.5))

from math import ceil, floor
round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

#Exercise - Convert strings to numbers and use absolute values
first_planet_input=input("Enter the distance from the sun for the first planet in KM: ")
second_planet_input=input("Enter the distance from the sun for the second planet in KM: ")

first_planet=int(first_planet_input)
second_planet=int(second_planet_input)

distance_km=second_planet - first_planet
print(abs(distance_km))
