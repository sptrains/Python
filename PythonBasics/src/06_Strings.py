fact = "The Moon has no atmosphere. "
two_facts = fact + "No sound can be heard on the Moon."  #fact += "No sound can be here on the moon" #strings are immutable
print(two_facts)

moon_radius = "The Moon has a radius of 1,080 miles."
print(moon_radius)

test='The "near side" is the part of the Moon that faces the Earth. '
test += "We only see about 60% of the Moon's surface."

test="""We only see about 60% of the Moon's surface, this is known as the "near side"."""
print(test)


multiline = "Facts about the Moon:\n There is no atomsphere.\n There is no sound."
print(multiline)


multiline2 = """Facts about the Moon: There is no atmosphere. There is no sound."""
print(multiline2)
