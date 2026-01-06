"""
Write a python function to compute the square root of a given non-negative number using the binary search algorithm.
"""
def square_root(n):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if n == 0 or n == 1:
        return n

    left = 0
    right = n
    mid = (left + right) / 2
    epsilon = 0.00001  # Precision level

    while abs(mid * mid - n) > epsilon:
        if mid * mid < n:
            left = mid
        else:
            right = mid
        mid = (left + right) / 2

    return mid
try:
    number = float(input("Enter a non-negative number to find its square root: "))
    result = square_root(number)
    print(f"The square root of {number} is approximately {result}.")
except ValueError as e:
    print(f"Invalid input. {e}")