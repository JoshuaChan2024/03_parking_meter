import math # <-- Import the math module for mathematical operations

def calculate_parking_fee(minutes):
    """Calculate the charge for a stay measured in whole minutes."""
    if type(minutes) is not int:
        raise TypeError("invalid argument type")
    
    if minutes < 0:
        raise ValueError("argument outside permitted range")
    
    return math.ceil(minutes / 60) * 200 # <-- Use math.ceil to round up to the nearest whole hour and multiply by 200 for the fee
