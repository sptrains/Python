# print("temperatures and facts about the moon".title())

# heading = "temperatures and facts about the moon"
# heading_upper = heading.title()
# print(heading_upper)

# temperatures = "Daylight: 260 F Nighttime: -280 F"
# temperatures_list = temperatures .split()
# print(temperatures_list)


# temperatures = "Daylight: 260 F\n Nighttime: -280 F"
# temperatures_list = temperatures.split('\n')
# print(temperatures_list)

#Search for a string

print("Moon" in "This text will describe facts and challenges with space travel")

print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper())

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[1])
print(parts[-1])