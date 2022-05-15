import math

def get_degree(rad):
    return f"The Degree is : {math.degrees(rad)}"


rad = float(input("Provide Radian value : "))
print(get_degree(rad))
