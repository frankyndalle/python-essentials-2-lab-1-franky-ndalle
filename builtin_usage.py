
import math
import random
import platform
import sys

number = random.randint(1, 100)
square_root = math.sqrt(number)
rounded_square_root = math.floor(square_root)

print("Random number:", number)
print("Square root rounded down:", rounded_square_root)
print("Operating system:", platform.system())
print("Python version:", sys.version)
