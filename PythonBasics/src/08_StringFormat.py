mass_percentage="1/6"
print("On the moon, you would weigh about %s of your weight on earth." %mass_percentage)

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

print("On the moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

print(f"On the moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.") #With f-strings, you don't need to assign a value to a variable beforehand:

subject="intresting facts about the moon"
heading=f"{subject.title()}"
print(heading)

# Exercise: Formatting strings
name="Ganymede"
planet="Mars"
gravity="1.43"

template="""Gravity Facts about {name}
----------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(f"{template.format(name=name,planet=planet,gravity=gravity)}")