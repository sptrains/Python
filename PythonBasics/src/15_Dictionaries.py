planet= {
    "name":"Earth",
    "moons":1
}
print(planet)
print(planet.get('name'))

print(planet["moons"])

# print(planet.get('wibble')) # Returns None
# print(planet['wibble']) # Throws KeyError

planet.update({
    'name':'Jupiter',
    'moons':'79'
})
print(planet)
print(planet.get('name'))
print(planet["moons"])

planet['orbital period']=4333
print(planet)
planet.pop("orbital period")
print(planet)

planet["diameter (km)"] = {
    'polar': 133709,
    'equatorial': 142984
}

print(planet)
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

planet = {
    'name':'Mars',
    'moons':2
}

print(f'{planet["name"]} has {planet["moons"]} moon(s)')

planet['circumference (km)']={
    'polar':6752,
    'equatorial':6792
}
print(planet)

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')