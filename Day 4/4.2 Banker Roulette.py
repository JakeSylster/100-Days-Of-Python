#Banker Roulette
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#My Solution
selector = random.randint(0,4)
# print(selector)
print(friends[selector])

#Instructor's Answer
print(random.choice(friends))
