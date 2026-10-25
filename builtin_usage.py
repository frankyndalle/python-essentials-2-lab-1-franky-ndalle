
import math
import random
import platform

# Generate a random integer between 1 and 100.
number = random.randint(1, 100)

# Calculate the square root and round it down.
square_root = math.sqrt(number)
rounded_square_root = math.floor(square_root)

# Get system information using the platform module.
operating_system = platform.system()
python_version = platform.python_version()

# Display the results with descriptive labels.
print("Random Number:", number)
print("Square Root (floored):", rounded_square_root)
print("Operating System:", operating_system)
print("Python Version:", python_version)
