# Client.py
import sys
from omniORB import CORBA

import CalculatorApp

# 1. Initialize the ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# 2. Read the IOR from the file
try:
    with open("ior.txt", "r") as f:
        ior = f.read()
except IOError:
    print("Error: Cannot open ior.txt. Is the server running?")
    sys.exit(1)

obj = orb.string_to_object(ior)

calc_obj = obj._narrow(CalculatorApp.Calculator)

if calc_obj is None:
    print("Object reference is not a Calculator object")
    sys.exit(1)

num1 = 100.5
num2 = 25.2

try:
    sum_result = calc_obj.add(num1, num2)
    diff_result = calc_obj.subtract(num1, num2)

    print(f"{num1} + {num2} = {sum_result}")
    print(f"{num1} - {num2} = {diff_result}")

except CORBA.Exception as e:
    print(f"A CORBA exception occurred: {e}")