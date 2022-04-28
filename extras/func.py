# extras/func.py
from os import system
from sys import platform
def clear():
    system("clear" if platform != "win32" and platform != "cygwin" and platform != "msys" else "cls")
    print("----------------------------------\n~~~~~~~~ Grade Calculator ~~~~~~~~\n----------------------------------\n")
def isAFloat(num):
    try: float(num); return True
    except ValueError: return False
def isAnInt(num):
    try: int(num); return True
    except ValueError: return False

