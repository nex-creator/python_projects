import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_no = random.randint(0,4)
person = friends[random_no]
print(person)
print(random.choice(friends))