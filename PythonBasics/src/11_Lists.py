planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print(planets)
print("The first Planet is", planets[0])
print("The second Planet is", planets[1])
print("The third Planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

number_of_planets=len(planets)
print("There are", number_of_planets, "planets in the solar system")
print(f"There are {number_of_planets} planets in the solar system")

planets.append("Pluto")
number_of_planets=len(planets)
print("There are actually", number_of_planets, "planets in the solar system")
print(planets)
planets.pop()
print(planets)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")


#Exercise - Create and use Python lists