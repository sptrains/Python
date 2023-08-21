# user_input = ''
# inputs=[]

# while user_input.lower() != "done":
#     if user_input:
#         inputs.append(user_input)
#     user_input=input("Enter a new value, or done when done: ")

# print(inputs)


#Exercise - Create a 'while' loop
new_planet = ''
planets = []

while new_planet.lower() != "done":
    if new_planet:
        planets.append(new_planet)
    new_planet=input("Enter new planet, or done if done: ")

print(planets)