#Welcome to Heads or Tails
# import random
# import my_module

# random_integer = random.randint(1,10)
# print(random_integer)
# print(my_module.my_favourite_number)
import random

random_number_0_to_1 = random.random()
#print(random_number_0_to_1)

random_float = random.uniform(1,10)
#print(random_float)

print("welcome to Heads or Tails")
if random_float <= 5:
    print("Heads")
else:
    print("Tales")
