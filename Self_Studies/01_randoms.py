import random
import string


# 1. Generate Random Numbers

print(random.random())  # Example: 0.675484
print(random.uniform(1, 10))  # Example: 7.236
print(random.randint(1, 10))  # Example: 4
print(random.randrange(0, 10, 2))  # Example: 2, 4, 6, or 8


# 2. Randomly Select from a Sequence

colors = ["red", "blue", "green"]
print(random.choice(colors))  # Example: "blue"

items = ["apple", "banana", "cherry"]
print(random.choices(items, weights=[1, 2, 1], k=5))  # Example: ['banana', 'apple', 'banana', 'cherry', 'banana']

print(random.sample(range(1, 11), 3))  # Example: [4, 1, 9]



# 3. Shuffle Data

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Example: [3, 1, 4, 5, 2]



# 4. Seed for Reproducibility

random.seed(42)
print(random.random())  # Example: 0.6394267984578837



# Example Use Cases

# 1. Generate a RAndom Password

def geneate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))


print(geneate_password(int(input("Enter a number"))))


# 2. Simulate a Dice Roll

def roll_dice():
    return random.randint(1,6)

print(roll_dice())