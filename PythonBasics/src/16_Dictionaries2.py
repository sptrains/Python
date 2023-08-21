rainfall = {
    'October':3.5,
    'November':4.2,
    'December':2.1
}
print(rainfall)
for key in rainfall:
    print(f'{key}:{rainfall[key]}cm')

if "October" in rainfall:
    rainfall['December']=rainfall['December'] +1
else:
    rainfall['December']=1

print(rainfall)

total_rainfall=0
for key in rainfall:
    total_rainfall = total_rainfall + rainfall[key]

print(f'There was {total_rainfall}cm in the last quarter.')


#Exercise - Dynamic programming with dictionaries

planet_moons = {
    'mercury': 0, 
    'venus': 0, 
    'earth': 1, 
    'mars': 2, 
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

total_moons=0
for moon in planet_moons: total_moons = total_moons + planet_moons[moon]
print(total_moons)

total_planets=len(planet_moons.keys())
print("Number of planets in solar system: ", total_planets)
moons=planet_moons.values()
print("Number of moons in Solar system:", sum(moons))
from math import ceil, floor
print("Each planet has an average of ", floor(total_moons/total_planets), " moons.")