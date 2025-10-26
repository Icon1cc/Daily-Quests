# DSA Mathematics - Complete Notes

## Table of Contents
1. [Sum of Natural Numbers](#1-sum-of-natural-numbers)
2. [Count Digits](#2-count-digits)
3. [Palindrome Number](#3-palindrome-number)
4. [Factorial of a Number](#4-factorial-of-a-number)
5. [Prime Factorization](#5-prime-factorization)
6. [All Divisors of a Number](#6-all-divisors-of-a-number)
7. [Sieve of Eratosthenes](#7-sieve-of-eratosthenes)
8. [Computing Power](#8-computing-power)

---

## 1. Sum of Natural Numbers

### Problem Statement
Given a number `n`, find the sum of first `n` natural numbers.

**Formula:** 1 + 2 + 3 + ... + n

### Examples
```
Input: n = 3
Output: 6
Explanation: 1 + 2 + 3 = 6

Input: n = 5
Output: 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15
```

---

### Approach 1: Iterative (Naive)

**Concept:** Use a loop to add all numbers from 1 to n.

```python
def findSum(n):
    sum = 0
    for x in range(1, n + 1):
        sum = sum + x
    return sum

# Test
n = 5
print(findSum(n))  # Output: 15
```

**Time Complexity:** O(n) - We iterate through n numbers  
**Space Complexity:** O(1) - Only using a few variables

**Dry Run for n = 5:**
```
Iteration 1: sum = 0 + 1 = 1
Iteration 2: sum = 1 + 2 = 3
Iteration 3: sum = 3 + 3 = 6
Iteration 4: sum = 6 + 4 = 10
Iteration 5: sum = 10 + 5 = 15
Final Answer: 15
```

---

### Approach 2: Mathematical Formula (Efficient)

**Concept:** Use the mathematical formula: **sum = n × (n + 1) / 2**

**Mathematical Proof:**
```
For n = 5:
sum = 5 × (5 + 1) / 2
    = 5 × 6 / 2
    = 30 / 2
    = 15 ✓
```

**Why this formula works:**
```
Let S = 1 + 2 + 3 + ... + n
Also S = n + (n-1) + (n-2) + ... + 1 (reverse order)

Adding both:
2S = (1+n) + (2+n-1) + (3+n-2) + ... + (n+1)
2S = (n+1) + (n+1) + (n+1) + ... + (n+1)  [n times]
2S = n(n+1)
S = n(n+1)/2
```

```python
def findSum(n):
    return n * (n + 1) // 2

# Test
n = 5
print(findSum(n))  # Output: 15
```

**Time Complexity:** O(1) - Direct formula calculation  
**Space Complexity:** O(1) - No extra space

---

### Approach 3: Overflow Prevention

**Concept:** To prevent overflow for large numbers, divide first (either n or n+1 will be even).

```python
def findSum(n):
    if n % 2 == 0:
        # n is even, so divide n by 2
        return (n // 2) * (n + 1)
    else:
        # n is odd, so (n+1) is even, divide (n+1) by 2
        return ((n + 1) // 2) * n

# Test
n = 5
print(findSum(n))  # Output: 15
```

**Example:**
- For n = 5 (odd): ((5+1)//2) × 5 = 3 × 5 = 15
- For n = 6 (even): (6//2) × (6+1) = 3 × 7 = 21

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

---

## 2. Count Digits

### Problem Statement
Given a number `n`, count the number of digits in it.

### Examples
```
Input: 256
Output: 3

Input: 75
Output: 2

Input: 5
Output: 1

Input: 9542
Output: 4
```

---

### Approach: Iterative Division

**Concept:** Keep dividing the number by 10 until it becomes 0. Count each division.

**How it works:**
- Each division by 10 removes the rightmost digit
- Count how many times we can divide until number becomes 0

```python
def countDigits(n):
    # Handle edge case for 0
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        n = n // 10  # Remove last digit
        count += 1
    
    return count

# Test
x = 9542
print("Count of digits:", countDigits(x))  # Output: 4
```

**Time Complexity:** O(d) where d = number of digits  
**Space Complexity:** O(1)

---

**Dry Run for n = 9542:**

```
Initial: n = 9542, count = 0

Iteration 1:
  n = 9542 // 10 = 954
  count = 1

Iteration 2:
  n = 954 // 10 = 95
  count = 2

Iteration 3:
  n = 95 // 10 = 9
  count = 3

Iteration 4:
  n = 9 // 10 = 0
  count = 4

Loop ends (n = 0)
Final Answer: 4 digits
```

---

### Visual Representation

```
9542 → 954 → 95 → 9 → 0
 ↓      ↓     ↓    ↓
 1      2     3    4 digits
```

---

### Alternative: Using Math

```python
import math

def countDigits(n):
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1

# Test
print(countDigits(9542))  # Output: 4
```

**Why this works:**
- log₁₀(9542) ≈ 3.98
- floor(3.98) = 3
- 3 + 1 = 4 digits ✓

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

---

## 3. Palindrome Number

### Problem Statement
Check if a given number is a palindrome. A number is palindrome if it reads the same forwards and backwards.

### Examples
```
Input: 78987
Output: Yes (reads same both ways)

Input: 8668
Output: Yes

Input: 8
Output: Yes (single digit)

Input: 21
Output: No (12 ≠ 21)

Input: 837
Output: No (738 ≠ 837)
```

---

### Approach: Reverse and Compare

**Concept:** Reverse the number and compare with the original. If they match, it's a palindrome.

**Algorithm:**
1. Store the original number
2. Reverse the number digit by digit
3. Compare reversed number with original

```python
def isPalindrome(n):
    # Negative numbers are not palindromes
    if n < 0:
        return False
    
    rev = 0
    temp = n
    
    # Reverse the number
    while temp != 0:
        last_digit = temp % 10      # Get last digit
        rev = rev * 10 + last_digit  # Add to reversed number
        temp = temp // 10            # Remove last digit
    
    # Check if reversed equals original
    return rev == n

# Test
print(isPalindrome(78987))  # Output: True
print(isPalindrome(21))     # Output: False
```

**Time Complexity:** O(d) where d = number of digits  
**Space Complexity:** O(1)

---

**Dry Run for n = 3443:**

```
Initial: n = 3443, temp = 3443, rev = 0

Iteration 1:
  last_digit = 3443 % 10 = 3
  rev = 0 * 10 + 3 = 3
  temp = 3443 // 10 = 344

Iteration 2:
  last_digit = 344 % 10 = 4
  rev = 3 * 10 + 4 = 34
  temp = 344 // 10 = 34

Iteration 3:
  last_digit = 34 % 10 = 4
  rev = 34 * 10 + 4 = 344
  temp = 34 // 10 = 3

Iteration 4:
  last_digit = 3 % 10 = 3
  rev = 344 * 10 + 3 = 3443
  temp = 3 // 10 = 0

Loop ends
rev = 3443, n = 3443
3443 == 3443 → True (Palindrome!)
```

---

**Visual Process:**

```
Original: 3443
          ↓
Extract:  3 → 4 → 4 → 3
          ↓   ↓   ↓   ↓
Build:    3→34→344→3443
          ↓
Reversed: 3443
          ↓
Compare: 3443 == 3443 ✓
```

---

## 4. Factorial of a Number

### Problem Statement
Calculate the factorial of a number n, denoted as n!

**Definition:** n! = n × (n-1) × (n-2) × ... × 2 × 1

**Special Cases:**
- 0! = 1
- 1! = 1

### Examples
```
Input: 4
Output: 24
Explanation: 4! = 4 × 3 × 2 × 1 = 24

Input: 6
Output: 720
Explanation: 6! = 6 × 5 × 4 × 3 × 2 × 1 = 720

Input: 0
Output: 1

Input: 1
Output: 1
```

---

### Approach 1: Iterative

**Concept:** Multiply numbers from 1 to n using a loop.

```python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test
print(factorial(5))  # Output: 120
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Dry Run for n = 5:**
```
Initial: result = 1

i = 2: result = 1 × 2 = 2
i = 3: result = 2 × 3 = 6
i = 4: result = 6 × 4 = 24
i = 5: result = 24 × 5 = 120

Final Answer: 120
```

---

### Approach 2: Recursive

**Concept:** Define factorial recursively: n! = n × (n-1)!

**Base case:** 0! = 1

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Test
print(factorial(5))  # Output: 120
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Due to recursion stack

**Recursion Tree for n = 5:**
```
factorial(5)
  = 5 × factorial(4)
      = 4 × factorial(3)
          = 3 × factorial(2)
              = 2 × factorial(1)
                  = 1 (base case)
              = 2 × 1 = 2
          = 3 × 2 = 6
      = 4 × 6 = 24
  = 5 × 24 = 120
```

**Call Stack:**
```
factorial(5)  ← Waiting for factorial(4)
factorial(4)  ← Waiting for factorial(3)
factorial(3)  ← Waiting for factorial(2)
factorial(2)  ← Waiting for factorial(1)
factorial(1)  → Returns 1
factorial(2)  → Returns 2
factorial(3)  → Returns 6
factorial(4)  → Returns 24
factorial(5)  → Returns 120
```

---

## 5. Prime Factorization

### Problem Statement
Find all prime factors of a given number n.

**Definition:** Prime factorization is expressing a number as a product of its prime factors.

### Examples
```
Input: 12
Output: 2 2 3
Explanation: 12 = 2² × 3

Input: 315
Output: 3 3 5 7
Explanation: 315 = 3² × 5 × 7

Input: 100
Output: 2 2 5 5
Explanation: 100 = 2² × 5²
```

---

### Approach 1: Naive Method

**Concept:** Check divisibility from 2 to n.

```python
def primeFactors(n):
    # Handle 2 separately
    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2
    
    # Check odd numbers from 3 onwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n = n // i
        i += 2
    
    # If n is still greater than 1, then it's a prime
    if n > 1:
        print(n, end=" ")

# Test
primeFactors(315)  # Output: 3 3 5 7
```

**Time Complexity:** O(√n)  
**Space Complexity:** O(1)

---

**Dry Run for n = 100:**

```
Step 1: Check divisibility by 2
  100 % 2 == 0 → Print 2, n = 100//2 = 50
  50 % 2 == 0 → Print 2, n = 50//2 = 25
  25 % 2 != 0 → Move to next

Step 2: Check odd numbers (i = 3)
  25 % 3 != 0 → Move to next

Step 3: Check i = 5
  25 % 5 == 0 → Print 5, n = 25//5 = 5
  5 % 5 == 0 → Print 5, n = 5//5 = 1
  
Step 4: n = 1, stop

Output: 2 2 5 5
Prime factorization: 100 = 2² × 5²
```

---

### Visual Factorization Tree

```
       100
       / \
      2   50
          / \
         2   25
             / \
            5   5

Prime Factors: 2, 2, 5, 5
```

---

### Approach 2: Efficient Division

**Concept:** Divide by smallest factors first, automatically ensures prime factors.

```python
def primeFactors(n):
    factors = []
    
    # Remove all 2s
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check odd divisors from 3 to √n
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    
    # If n > 1, then it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors

# Test
print(primeFactors(315))  # Output: [3, 3, 5, 7]
```

**Why this works:**
- We start with smallest factors (2, then odd numbers)
- Any composite number would have been divided out earlier
- Only prime factors remain

---

## 6. All Divisors of a Number

### Problem Statement
Find all divisors (factors) of a given number n.

**Definition:** A divisor of n is a number that divides n completely (remainder = 0).

### Examples
```
Input: n = 10
Output: 1 2 5 10

Input: n = 100
Output: 1 2 4 5 10 20 25 50 100

Input: n = 125
Output: 1 5 25 125
```

---

### Approach 1: Naive Method

**Concept:** Check every number from 1 to n for divisibility.

```python
def printDivisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Test
print(printDivisors(100))
# Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1) [excluding output storage]

**Dry Run for n = 12:**
```
i = 1:  12 % 1 = 0 ✓ → Add 1
i = 2:  12 % 2 = 0 ✓ → Add 2
i = 3:  12 % 3 = 0 ✓ → Add 3
i = 4:  12 % 4 = 0 ✓ → Add 4
i = 5:  12 % 5 = 2 ✗
i = 6:  12 % 6 = 0 ✓ → Add 6
i = 7:  12 % 7 = 5 ✗
i = 8:  12 % 8 = 4 ✗
i = 9:  12 % 9 = 3 ✗
i = 10: 12 % 10 = 2 ✗
i = 11: 12 % 11 = 1 ✗
i = 12: 12 % 12 = 0 ✓ → Add 12

Divisors: [1, 2, 3, 4, 6, 12]
```

---

### Approach 2: Optimized (Using √n)

**Concept:** Divisors come in pairs! If i divides n, then n/i also divides n.

**Key Insight:**
- For n = 100: divisors are (1,100), (2,50), (4,25), (5,20), (10,10)
- We only need to check up to √n

```python
import math

def printDivisors(n):
    divisors = []
    
    # Check from 1 to √n
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            divisors.append(i)
            
            # Add the pair divisor (avoid duplicates for perfect squares)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    
    return sorted(divisors)

# Test
print(printDivisors(100))
# Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]
```

**Time Complexity:** O(√n)  
**Space Complexity:** O(1)

---

**Dry Run for n = 36:**

```
√36 = 6, so check i from 1 to 6

i = 1: 36 % 1 = 0 ✓
  → Add 1 and 36/1 = 36
  Divisors: [1, 36]

i = 2: 36 % 2 = 0 ✓
  → Add 2 and 36/2 = 18
  Divisors: [1, 36, 2, 18]

i = 3: 36 % 3 = 0 ✓
  → Add 3 and 36/3 = 12
  Divisors: [1, 36, 2, 18, 3, 12]

i = 4: 36 % 4 = 0 ✓
  → Add 4 and 36/4 = 9
  Divisors: [1, 36, 2, 18, 3, 12, 4, 9]

i = 5: 36 % 5 = 1 ✗
  → Skip

i = 6: 36 % 6 = 0 ✓
  → Add 6 (36/6 = 6, don't add duplicate)
  Divisors: [1, 36, 2, 18, 3, 12, 4, 9, 6]

After sorting: [1, 2, 3, 4, 6, 9, 12, 18, 36]
```

---

### Visual Representation of Divisor Pairs

```
n = 100

Pair 1:  1 × 100 = 100
Pair 2:  2 × 50  = 100
Pair 3:  4 × 25  = 100
Pair 4:  5 × 20  = 100
Pair 5: 10 × 10  = 100 (same number, count once)

All divisors: 1, 2, 4, 5, 10, 20, 25, 50, 100
```

---

## 7. Sieve of Eratosthenes

### Problem Statement
Find all prime numbers less than or equal to a given number n.

**Definition:** An efficient algorithm to find all primes up to n.

### Examples
```
Input: n = 10
Output: 2 3 5 7

Input: n = 20
Output: 2 3 5 7 11 13 17 19

Input: n = 30
Output: 2 3 5 7 11 13 17 19 23 29
```

---

### Algorithm: Sieve of Eratosthenes

**Concept:** Mark multiples of each prime as composite (not prime).

**Steps:**
1. Create a boolean array of size n+1, initially all True
2. Mark 0 and 1 as not prime
3. For each number p from 2 to √n:
   - If p is still marked as prime
   - Mark all multiples of p (starting from p²) as not prime
4. All remaining True values are primes

```python
def sieveOfEratosthenes(n):
    # Create a boolean array and initialize all as True
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime
    
    p = 2
    while p * p <= n:
        # If prime[p] is still True, it's a prime
        if prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = []
    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)
    
    return primes

# Test
print(sieveOfEratosthenes(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

**Time Complexity:** O(n log(log n))  
**Space Complexity:** O(n)

---

**Dry Run for n = 20:**

```
Step 1: Initialize array
prime = [F, F, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T]
Index:   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20

Step 2: p = 2 (first prime)
  Mark multiples: 4, 6, 8, 10, 12, 14, 16, 18, 20
prime = [F, F, T, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F]

Step 3: p = 3
  Mark multiples: 9, 12, 15, 18
prime = [F, F, T, T, F, T, F, T, F, F, F, T, F, T, F, F, F, T, F, T, F]

Step 4: p = 5 (5² = 25 > 20, so stop)

Step 5: Collect primes
Indices where prime[i] = True: 2, 3, 5, 7, 11, 13, 17, 19

Output: [2, 3, 5, 7, 11, 13, 17, 19]
```

---

### Visual Process for n = 30

```
Initial: All numbers 2-30 marked as potential primes

After marking multiples of 2:
2  3  ✗  5  ✗  7  ✗  9  ✗ 11  ✗ 13  ✗ 15  ✗ 17  ✗ 19  ✗ 21  ✗ 23  ✗ 25  ✗ 27  ✗ 29  ✗

After marking multiples of 3:
2  3  ✗  5  ✗  7  ✗  ✗  ✗ 11  ✗ 13  ✗  ✗  ✗ 17  ✗ 19  ✗  ✗  ✗ 23  ✗ 25  ✗  ✗  ✗ 29  ✗

After marking multiples of 5:
2  3  ✗  5  ✗  7  ✗  ✗  ✗ 11  ✗ 13  ✗  ✗  ✗ 17  ✗ 19  ✗  ✗  ✗ 23  ✗  ✗  ✗  ✗  ✗ 29  ✗

Remaining primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
```

---

### Why Start from p²?

**Key Insight:** Multiples less than p² have already been marked by smaller primes.

Example for p = 5:
- 5×2=10 already marked by 2
- 5×3=15 already marked by 3
- 5×4=20 already marked by 2
- 5×5=25 not yet marked ← Start here!

---

## 8. Computing Power

### Problem Statement
Compute x^n (x raised to the power n) efficiently.

### Examples
```
Input: x = 2, n = 3
Output: 8
Explanation: 2³ = 2 × 2 × 2 = 8

Input: x = 7, n = 2
Output: 49
Explanation: 7² = 7 × 7 = 49

Input: x = 5, n = 0
Output: 1
Explanation: Any number to power 0 is 1
```

---

### Approach 1: Naive Iterative

**Concept:** Multiply x by itself n times.

```python
def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

# Test
print(power(2, 3))  # Output: 8
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Dry Run for power(2, 5):**
```
Initial: result = 1

Iteration 1: result = 1 × 2 = 2
Iteration 2: result = 2 × 2 = 4
Iteration 3: result = 4 × 2 = 8
Iteration 4: result = 8 × 2 = 16
Iteration 5: result = 16 × 2 = 32

Final Answer: 32
```

---

### Approach 2: Recursive (Divide and Conquer)

**Concept:** Use the properties:
- x^n = (x^(n/2))² if n is even
- x^n = x × (x^(n/2))² if n is odd

**This is the same algorithm we discussed earlier!**

```python
def power(x, n):
    # Base case
    if n == 0:
        return 1
    
    # Handle negative exponents
    if n < 0:
        x = 1 / x
        n = -n
    
    # Recursive calculation
    half = power(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half

# Test
print(power(2, 5))   # Output: 32
print(power(3, 4))   # Output: 81
print(power(2, -3))  # Output: 0.125
```

**Time Complexity:** O(log n)  
**Space Complexity:** O(log n) - Recursion stack

---

**Dry Run for power(2, 5):**

```
Call 1: power(2, 5)
  ├─ n = 5 (odd)
  ├─ half = power(2, 2)
  │    ├─ n = 2 (even)
  │    ├─ half = power(2, 1)
  │    │    ├─ n = 1 (odd)
  │    │    ├─ half = power(2, 0)
  │    │    │    └─ Returns 1
  │    │    ├─ half = 1
  │    │    └─ Returns 2 × 1 × 1 = 2
  │    ├─ half = 2
  │    └─ Returns 2 × 2 = 4
  ├─ half = 4
  └─ Returns 2 × 4 × 4 = 32

Final Answer: 32
```

---

### Approach 3: Iterative Binary Exponentiation

**Concept:** Convert the exponent to binary and use bit manipulation.

**Key Idea:**
- 5 in binary = 101
- 2^5 = 2^(4+1) = 2^4 × 2^1 = 16 × 2 = 32

```python
def power(x, n):
    # Handle negative exponents
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1
    
    while n > 0:
        # If n is odd, multiply result by x
        if n % 2 == 1:
            result *= x
        
        # Square x and halve n
        x *= x
        n //= 2
    
    return result

# Test
print(power(2, 5))   # Output: 32
print(power(3, 4))   # Output: 81
```

**Time Complexity:** O(log n)  
**Space Complexity:** O(1) - No recursion!

---

**Dry Run for power(2, 5):**

```
Initial: x = 2, n = 5, result = 1

Iteration 1:
  n % 2 = 5 % 2 = 1 (odd) → result = 1 × 2 = 2
  x = 2 × 2 = 4
  n = 5 // 2 = 2

Iteration 2:
  n % 2 = 2 % 2 = 0 (even) → result stays 2
  x = 4 × 4 = 16
  n = 2 // 2 = 1

Iteration 3:
  n % 2 = 1 % 2 = 1 (odd) → result = 2 × 16 = 32
  x = 16 × 16 = 256
  n = 1 // 2 = 0

Loop ends (n = 0)
Final Answer: 32
```

---

**How Binary Exponentiation Works:**

```
2^5 = 2^(101₂)
    = 2^(4+0+1)
    = 2^4 × 2^1
    
Bit by bit:
Bit 0 (rightmost): 1 → Multiply by 2^1 = 2
Bit 1 (middle):    0 → Skip
Bit 2 (leftmost):  1 → Multiply by 2^4 = 16

Result: 2 × 16 = 32
```

---

### Visual Comparison of Approaches

```
Calculate 2^10 = 1024

Naive Approach:
2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2
10 multiplications

Binary Exponentiation:
2^10 = 2^(8+2) = 2^8 × 2^2
     = 256 × 4
Only 4 squaring operations!

Steps:
2^1 = 2
2^2 = 4
2^4 = 16
2^8 = 256
2^10 = 256 × 4 = 1024
```

---

## Summary Table

| Problem | Naive Time | Optimized Time | Space | Key Technique |
|---------|------------|----------------|-------|---------------|
| Sum of N numbers | O(n) | O(1) | O(1) | Mathematical formula |
| Count Digits | O(d) | O(1) | O(1) | Log formula or division |
| Palindrome | O(d) | O(d) | O(1) | Reverse and compare |
| Factorial | O(n) | O(n) | O(n) | Recursion or iteration |
| Prime Factors | O(n) | O(√n) | O(1) | Check up to √n |
| All Divisors | O(n) | O(√n) | O(1) | Divisor pairs |
| Sieve | N/A | O(n log log n) | O(n) | Mark multiples |
| Power | O(n) | O(log n) | O(log n) or O(1) | Binary exponentiation |

---

## Key Concepts to Remember

### 1. Square Root Optimization
Many problems only need checking up to √n:
- Prime checking
- Finding divisors
- Prime factorization

### 2. Mathematical Formulas
Direct formulas can reduce O(n) to O(1):
- Sum of n numbers: n(n+1)/2
- Count digits: floor(log₁₀(n)) + 1

### 3. Divide and Conquer
Splitting problems in half gives O(log n):
- Binary exponentiation
- Binary search

### 4. Sieving Technique
Pre-compute answers for multiple queries:
- Sieve of Eratosthenes for primes

### 5. Bit Manipulation
Binary representation can optimize operations:
- Fast power calculation
- Checking even/odd with n & 1

---

## Practice Problems

### Easy
1. Find sum of digits of a number
2. Check if a number is prime
3. Find GCD of two numbers
4. Count trailing zeros in factorial

### Medium
1. Find all prime factors with their powers
2. Find nth Fibonacci number efficiently
3. Compute modular exponentiation
4. Find LCM of array elements

### Hard
1. Count primes in range [L, R]
2. Find all divisors in O(√n) sorted order
3. Segmented Sieve
4. Fast matrix exponentiation

---

## Common Pitfalls

1. **Integer Overflow:** Use appropriate data types (long long in C++)
2. **Off-by-one Errors:** Be careful with loop boundaries
3. **Edge Cases:** Test with n=0, n=1, negative numbers
4. **Time Limits:** Choose correct algorithm for given constraints
5. **Space Optimization:** Iterative solutions use less space than recursive

---

## Tips for Interviews

1. **Always discuss approach first** before coding
2. **Mention time and space complexity**
3. **Test with examples** including edge cases
4. **Optimize step by step** - don't jump to optimal solution
5. **Explain your thought process** clearly

---

**Good luck with your DSA preparation! 🚀**

*Come back to these notes anytime you need a refresher. Everything is explained from first principles!*