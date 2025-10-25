"""
Write a Python function to find the prime factorization of a given number.
"""

def prime_factorization(n):
    """
    Finds the prime factorization of a given number.
    Returns a list of prime factors.
    """
    
    # Create a list to store the prime factors
    factors = []
    
    # Handle negative numbers and 0/1
    if n <= 1:
        return [] # 0, 1, and negatives have no prime factorization

    # --- Step 1: Handle the factor 2 ---
    # Continuously divide by 2 until it's no longer even
    while n % 2 == 0:
        factors.append(2)
        n //= 2 # Integer division
        
    # At this point, n is guaranteed to be odd.

    # --- Step 2: Handle odd prime factors ---
    # We can now check only odd numbers starting from 3
    # We only need to check up to the square root of the *remaining* n
    i = 3
    while i * i <= n:
        # Check if i is a factor. If it is, keep dividing by it.
        # This handles repeated factors (e.g., 9 = 3 * 3)
        while n % i == 0:
            factors.append(i)
            n //= i
        
        # Move to the next odd number
        i += 2
        
    # --- Step 3: Handle the last remaining prime ---
    # If n is still greater than 2 after the loop,
    # it means the remaining n is a prime number itself.
    # (e.g., if n was 14, we'd divide by 2, n becomes 7.
    # The loop above won't run. The remaining n=7 is prime.)
    if n > 2:
        factors.append(n)
        
    return factors

# --- Main part of the script ---
try:
    num = int(input("Enter a number: "))
    
    result = prime_factorization(num)
    
    print(f"The prime factorization of {num} is: {result}")

except ValueError:
    print("Invalid input. Please enter a whole number.")