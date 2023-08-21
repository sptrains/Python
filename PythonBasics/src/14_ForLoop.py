planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])

from time import sleep
countdown=[4,3,2,1,0]
for number in countdown:
    print(number)
    sleep(1) #wait 1 second
print("Blast off!! 🚀")