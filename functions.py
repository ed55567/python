# function
def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station")
    print("Take the Northbound N, Q, R, or W train 1 stop")
    print("Get off the Times Square 42nd Street stop")


directions_to_timesSq()

# calling function
print("Checking the weather for you!")


def weather_check():
    print("Looks great outside! Enjoy your trip.")


print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()

# Parameters & Arguments


def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)


# Checkpoint 3 & 4
generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")

# Multiple Parameters


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):

    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10

    print(car_rental_total + hotel_total + plane_ticket_price)


calculate_expenses(200, 100, 100, 5)

# Types of Arguments


def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in " + first_destination, "then " +
          second_destination, "and lastly " + final_destination)


trip_planner("London", "India", "New Zealand")
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland",
             final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")
