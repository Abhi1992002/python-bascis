import numpy as np
print(np.pi)

# exception handling in python

try:
    a = int(input("Please enter the number : "))
    for i in range(1,11):
        print(f"{a} * {i} = {a*i}")
except ValueError as e:
    print("Please enter the right number")
    print(e)
except Exception as e:
    print("Something went wrong")
    print(e)