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

#Transform text
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)  #return false
print("temperatures" in text.lower())

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(moon_facts)
print(' '.join(moon_facts))


###Exercise


text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split('.')
print(sentences)

for sentence in sentences:
    if "temperature" in sentence:
        print(sentence)