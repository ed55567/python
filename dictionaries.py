sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)


# Make a Dictionary

translations = {"mountain": "orod", "bread": "bass",
                "friend": "mellon", "horse": "roch"}


children = {"von Trapp": ["Johannes", "Rosmarie",
                          "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}


animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)


user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": [
    "Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements['earth'])
print(zodiac_elements['fire'])


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": [
    "Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"


print(zodiac_elements["energy"])


caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30

try:
    print(caffeine_level['matcha'])
except KeyError:
    print("Unknown Caffeine Level")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)

print(tc_id)
print(stack_id)


available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20,
                   "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)


pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9,
                           "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) +
          " percent of " + occupation + "s.")
