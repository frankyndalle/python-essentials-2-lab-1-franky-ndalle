
# Install the required package by running: python -m pip install colorama

from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.GREEN + "Colorama is working!")
print(Fore.YELLOW + "This message is yellow.")
print(Style.BRIGHT + Fore.CYAN + "This message is bright cyan.")
