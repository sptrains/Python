sum = 1 + 2
print(sum)

print("Show this in the console")

#print["Show this in the console"]

sum = 1 + 2 # 3
product = sum * 2
print(product)



#Data types

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type(distance_to_alpha_centauri)) ## <class 'float'>


#Operators

left_side = 10
right_side = 5
result=left_side / right_side # 2
print(result)

from datetime import date

#Data type conversion
print("Today date is :" + str(date.today()))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")