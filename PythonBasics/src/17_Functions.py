def rocket_parts():
    print('payload, propellant, strcuture')

rocket_parts()

output=rocket_parts()

any([True, False, False])

print(any([True, False, False, True]))
print(any([False, False, False, False]))

print(any([]))

print(str())
print(str(15))

def distance_from_earth(destination):
    if destination=='Moon':
        return 238855
    else:
        return "Unabale to compute to that destination"
    
print(distance_from_earth("Moon"))

def days_to_complete(distance, speed):
    hours=distance/speed
    return hours/24
print(days_to_complete(238855, 75))
print(round(days_to_complete(distance_from_earth("Moon"), 75)))


#Exercise: Work with arguments in functions
#===================================================================
def generate_report(main_tank, external_tank, hyderogen_tank):
    output=f"""Full Report:
    Main Tank:{main_tank}
    External Tank:{external_tank}
    Hydrogen Tank: {hyderogen_tank}"""
    print(output)

generate_report(100,70,50)

#====================================================================
from datetime import datetime, timedelta
def arrival_time(hours=51):
    now=datetime.now()
    arrival=now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())
print(arrival_time(10))
print(arrival_time(hours=10))

#====================================================================

def arrival_time(destination, hours=51):
    now=datetime.now()
    arrival=now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Moon"))
print(arrival_time("Orbit", hours=0.13))

#===================================================================

def variable_length(*args):
    print(args)

variable_length()
variable_length("one")
variable_length("one", "two")
variable_length(None)

#===================================================================

def sequnce_time(*args):
    total_minutes=sum(args)
    if total_minutes <60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} minutes"
    
print(sequnce_time())
print(sequnce_time(10,20,30))
print(sequnce_time(11,20,30))

#===================================================================

#https://learn.microsoft.com/en-us/training/modules/functions-python/6-variable-arguments