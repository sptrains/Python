gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
print(min(gravity_on_planets))
print(max(gravity_on_planets))

bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weight", bus_weight, "kg")
print("On Mercury, a double-decker bus weight", bus_weight * gravity_on_planets[0], "kg")

print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")


#Slice lists
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2] #slice
print(planets_before_earth)
planets_after_earth=planets[3:8]
print(planets_after_earth)

planets_after_earth = planets[3:]
print(planets_after_earth)


#Join lists
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons =amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

#Sort lists
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)


#Exercise - Work with list data

user_planet = input("Please enter the name of the planet (with a capital letter to start) ")
user_planet_index=planets.index(user_planet)
print(user_planet_index)
print("Here are the planets close than " + user_planet)
print(planets[0:user_planet_index])

print("Here are the planets after than " + user_planet)
print(planets[user_planet_index+1:])