# While Loop Walkthrough
# count = 0
# print("Starting While Loop")
# while count <= 3:
#   # Loop Body
#   # Print if the condition is still true
#   print("Loop Iteration - count <= 3 is still true")
#   # Print the current value of count
#   print("Count is currently " + str(count))
#   # Increment count
#   count += 1
#   print(" ----- ")
# print("While Loop ended")


countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")

# while loops
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1

# Infinite Loops
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    # students_period_A.append(student)
    print(student)

# Loop Control Break
dog_breeds_available_for_adoption = [
    "french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    break
if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")

# Loop Control: Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age < 21:
        continue
    print(age)


# Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]


scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)
