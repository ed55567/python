from library import always_three
from decimal import Decimal
from matplotlib import pyplot as plt
import codecademylib3_seaborn
import random
from datetime import datetime

current_time = datetime.now()

print(current_time)


# Create random_list below:
random_list = [random.randint(1, 100) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)


# Add your code below:


numbers_a = range(1, 13)

numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)

plt.show()


# Import Decimal below:

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# Import library below:
from library import always_three


# Call your function below:
always_three()
