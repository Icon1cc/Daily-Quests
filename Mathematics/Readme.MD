# DSA Mathematics - Theory & Concepts

## Table of Contents
1. [Sum of Natural Numbers](#1-sum-of-natural-numbers)
2. [Count Digits](#2-count-digits)
3. [Palindrome Number](#3-palindrome-number)
4. [Factorial of a Number](#4-factorial-of-a-number)
5. [Trailing Zeros in Factorial](#5-trailing-zeros-in-factorial)
6. [Prime Factorization](#6-prime-factorization)
7. [All Divisors of a Number](#7-all-divisors-of-a-number)
8. [Sieve of Eratosthenes](#8-sieve-of-eratosthenes)
9. [Computing Power](#9-computing-power)
10. [Binary Exponentiation](#10-binary-exponentiation)

---

## 1. Sum of Natural Numbers

### What is it?
The sum of first n natural numbers means adding all positive integers from 1 up to n.

**Examples:**
- First 3 numbers: 1 + 2 + 3 = 6
- First 5 numbers: 1 + 2 + 3 + 4 + 5 = 15
- First 100 numbers: 1 + 2 + 3 + ... + 100 = 5050

### The Story Behind the Formula
There's a famous story about young Carl Friedrich Gauss (a brilliant mathematician). His teacher asked the class to sum numbers 1 to 100 to keep them busy. Gauss found the answer in seconds!

**His clever observation:**
If you write the numbers forward and backward:
```
Forward:  1   +   2   +   3   + ... +  98  +  99  + 100
Backward: 100 +  99  +  98  + ... +   3  +   2  +   1
────────────────────────────────────────────────────────
Sum each: 101 + 101 + 101 + ... + 101 + 101 + 101
```

Each pair sums to 101, and there are 100 such pairs. Total = 101 × 100 = 10,100

But we counted everything twice! So the actual sum = 10,100 ÷ 2 = 5,050

### The Mathematical Formula
```
Sum of first n natural numbers = n × (n + 1) / 2
```

**Why does this work mathematically?**
- When you pair numbers from start and end, each pair sums to (n + 1)
- You have n numbers total, making n/2 pairs
- Therefore: (n + 1) × (n/2) = n(n + 1)/2

### Different Approaches

**Approach 1: Iterative (Brute Force)**
- Logic: Simply add numbers one by one from 1 to n
- Start with sum = 0
- Keep adding: sum = sum + 1, then sum = sum + 2, and so on
- Time: O(n) - need to do n additions
- Space: O(1) - only storing the sum

**Approach 2: Direct Formula**
- Logic: Use the mathematical formula directly
- Calculate: n × (n + 1) / 2
- Time: O(1) - just one calculation
- Space: O(1)

**Approach 3: Safe from Overflow**
- Logic: In programming, multiplying two large numbers first can cause overflow
- Better approach: Divide first, then multiply
- If n is even: divide n by 2 first, then multiply by (n+1)
- If n is odd: divide (n+1) by 2 first, then multiply by n
- This ensures one number is always even and divisible by 2

### Key Insight
Never iterate when you have a mathematical formula! O(1) beats O(n) always.

---

## 2. Count Digits

### What is it?
Counting how many digits are present in a given number.

**Examples:**
- 256 has 3 digits
- 5 has 1 digit
- 9542 has 4 digits
- 1000000 has 7 digits

### The Core Logic
Think about what happens when you divide a number by 10:
- 9542 ÷ 10 = 954 (removed one digit)
- 954 ÷ 10 = 95 (removed another digit)
- 95 ÷ 10 = 9 (removed another digit)
- 9 ÷ 10 = 0 (removed last digit)

We divided 4 times = 4 digits!

### Different Approaches

**Approach 1: Repeated Division**
- Logic: Keep dividing by 10 until the number becomes 0
- Count how many times you divided
- Each division removes one digit from the right
- Time: O(d) where d is the number of digits
- Space: O(1)

**Step-by-step for 9542:**
1. Start: number = 9542, count = 0
2. Divide: 9542 ÷ 10 = 954, count = 1
3. Divide: 954 ÷ 10 = 95, count = 2
4. Divide: 95 ÷ 10 = 9, count = 3
5. Divide: 9 ÷ 10 = 0, count = 4
6. Stop when number = 0, return count = 4

**Approach 2: String Conversion**
- Logic: Convert number to string and count characters
- Simple but uses extra space
- Time: O(d)
- Space: O(d) - storing the string

**Approach 3: Logarithm**
- Logic: Mathematical property - log₁₀(n) gives you the power of 10
- For example: log₁₀(1000) = 3 (because 10³ = 1000)
- Number of digits = floor(log₁₀(n)) + 1
- Time: O(1)
- Space: O(1)

**Why logarithm works:**
- A number with d digits lies between 10^(d-1) and 10^d
- Taking log₁₀ of both sides: (d-1) ≤ log₁₀(n) < d
- Therefore: d = floor(log₁₀(n)) + 1

### Special Cases
- Zero has 1 digit (special definition)
- Negative numbers: count digits of absolute value

### Key Insight
The division method is most intuitive and commonly used in DSA. It directly manipulates the number's structure.

---

## 3. Palindrome Number

### What is it?
A palindrome number reads the same forwards and backwards.

**Examples:**
- 121 → reverse is 121 ✓ (palindrome)
- 12321 → reverse is 12321 ✓ (palindrome)
- 78987 → reverse is 78987 ✓ (palindrome)
- 123 → reverse is 321 ✗ (not palindrome)
- 8 → single digit ✓ (always palindrome)

### The Core Logic
To check if a number is palindrome:
1. Keep the original number safe
2. Build the reversed version digit by digit
3. Compare reversed with original

**How to reverse a number:**
Think of peeling digits from the right and building from the left:
- Extract last digit using: last_digit = number % 10
- Add it to reversed: reversed = reversed × 10 + last_digit
- Remove last digit from original: number = number ÷ 10
- Repeat until number becomes 0

### Step-by-Step Example for 3443

**Building the reverse:**
```
Original = 3443, Reversed = 0

Step 1: Last digit = 3443 % 10 = 3
        Reversed = 0 × 10 + 3 = 3
        Number = 3443 ÷ 10 = 344

Step 2: Last digit = 344 % 10 = 4
        Reversed = 3 × 10 + 4 = 34
        Number = 344 ÷ 10 = 34

Step 3: Last digit = 34 % 10 = 4
        Reversed = 34 × 10 + 4 = 344
        Number = 34 ÷ 10 = 3

Step 4: Last digit = 3 % 10 = 3
        Reversed = 344 × 10 + 3 = 3443
        Number = 3 ÷ 10 = 0

Final: Reversed = 3443, Original = 3443 → Match! ✓
```

### Mathematical Operations Used
- **Modulo (%)**: Extracts the last digit
  - 9542 % 10 = 2
  - 954 % 10 = 4
- **Integer Division (÷)**: Removes the last digit
  - 9542 ÷ 10 = 954
  - 954 ÷ 10 = 95
- **Multiplication & Addition**: Builds the reversed number
  - reversed × 10 shifts digits left
  - Adding new digit places it in ones position

### Complexity Analysis
- Time: O(d) where d is the number of digits
- Space: O(1) - only storing a few variables
- Must process every digit once

### Key Insight
You don't need to convert to string or array. Work directly with mathematical operations on the number itself.

---

## 4. Factorial of a Number

### What is it?
The factorial of a non-negative integer n (written as n!) is the product of all positive integers less than or equal to n.

**Formula:** n! = n × (n-1) × (n-2) × ... × 2 × 1

**Examples:**
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 4! = 4 × 3 × 2 × 1 = 24
- 3! = 3 × 2 × 1 = 6
- 2! = 2 × 1 = 2
- 1! = 1
- 0! = 1 (by mathematical convention)

### Why is 0! = 1?
This is a mathematical convention that makes formulas work consistently. Think of it as:
- "In how many ways can you arrange 0 items?" → 1 way (the empty arrangement)
- Also, by the pattern: 3! = 3 × 2!, so 1! = 1 × 0!, therefore 0! = 1

### Real-World Applications
- **Permutations**: Arranging n items = n!
- **Combinations**: Selecting items from a group
- **Probability**: Many probability formulas use factorials
- **Series expansions**: Taylor series, e^x, sin(x), etc.

### History
The exclamation mark notation (!) was introduced by French mathematician Christian Kramp in 1808.

### Different Approaches

**Approach 1: Iterative**
- Logic: Use a loop to multiply numbers from 1 to n
- Start with result = 1
- Multiply: result × 2, then × 3, then × 4, ... up to × n
- Time: O(n) - need n multiplications
- Space: O(1) - only storing result

**Approach 2: Recursive**
- Logic: Break problem into smaller subproblems
- Key insight: n! = n × (n-1)!
- Base case: 0! = 1 or 1! = 1
- Recursive case: multiply n by factorial of (n-1)
- Time: O(n) - still n multiplications
- Space: O(n) - recursion uses call stack

**Recursion visualization for 5!:**
```
factorial(5) calls → 5 × factorial(4)
                     ↓
factorial(4) calls → 4 × factorial(3)
                     ↓
factorial(3) calls → 3 × factorial(2)
                     ↓
factorial(2) calls → 2 × factorial(1)
                     ↓
factorial(1) returns → 1
                     ↑
Returns: 2 × 1 = 2
                     ↑
Returns: 3 × 2 = 6
                     ↑
Returns: 4 × 6 = 24
                     ↑
Returns: 5 × 24 = 120
```

### Important Considerations
- **Growth Rate**: Factorials grow VERY fast!
  - 10! = 3,628,800
  - 20! = 2,432,902,008,176,640,000
- **Overflow**: Large factorials exceed integer limits
- **Negative Numbers**: Factorial is undefined for negative integers

### Which Approach to Use?
- **Iterative**: Better for actual computation (less space)
- **Recursive**: More elegant and intuitive, good for understanding concept
- In practice, for large n, neither is practical - use logarithms or approximations like Stirling's formula

### Key Insight
Factorial is a building block for many mathematical concepts. However, in DSA problems, you often DON'T need to calculate the actual factorial - you can use mathematical properties instead!

---

## 5. Trailing Zeros in Factorial

### What is it?
Trailing zeros are the zeros at the end of a number.

**Examples:**
- 120 has 1 trailing zero
- 1000 has 3 trailing zeros
- 4500 has 2 trailing zeros
- 1234 has 0 trailing zeros

**Question:** Given n, how many trailing zeros are in n!?

### The Wrong Approach
❌ DON'T calculate n! and count zeros at the end
- Factorial grows too fast
- Will cause overflow
- Extremely inefficient

### The Brilliant Insight

**Where do trailing zeros come from?**
A trailing zero is created by a factor of 10.
And 10 = 2 × 5

So we need pairs of 2s and 5s in the prime factorization.

**Key observation:**
In any factorial, there are ALWAYS more 2s than 5s!
- Even numbers contribute 2s
- Only every 5th number contributes a 5

Therefore: **Count of trailing zeros = Count of 5s in the prime factorization of n!**

### How to Count 5s

**Not just numbers divisible by 5!**
Some numbers contribute multiple 5s:
- 5 contributes one 5
- 10 contributes one 5 (10 = 2 × 5)
- 15 contributes one 5
- 25 contributes TWO 5s (25 = 5 × 5)
- 50 contributes TWO 5s (50 = 2 × 5 × 5)
- 125 contributes THREE 5s (125 = 5 × 5 × 5)

### The Formula
```
Count = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ⌊n/625⌋ + ...
```

**What this means:**
- ⌊n/5⌋: Count numbers divisible by 5 (each gives one 5)
- ⌊n/25⌋: Count numbers divisible by 25 (each gives an extra 5)
- ⌊n/125⌋: Count numbers divisible by 125 (each gives another extra 5)
- Continue until 5^k > n

### Step-by-Step Example: n = 100

```
⌊100/5⌋   = ⌊20⌋   = 20  (numbers: 5,10,15,20,25,...,100)
⌊100/25⌋  = ⌊4⌋    = 4   (numbers: 25,50,75,100)
⌊100/125⌋ = ⌊0.8⌋  = 0   (no numbers ≥ 125)

Total = 20 + 4 + 0 = 24 trailing zeros in 100!
```

**Why this works:**
- All 20 multiples of 5 contribute at least one 5
- Among those, 4 are multiples of 25 (contribute an extra 5)
- Total 5s = 20 + 4 = 24
- Total 2s in 100! >> 24, so we have 24 pairs of (2,5)
- Therefore, 24 trailing zeros

### Another Example: n = 30

```
⌊30/5⌋  = 6  (numbers: 5,10,15,20,25,30)
⌊30/25⌋ = 1  (number: 25)
⌊30/125⌋ = 0

Total = 6 + 1 = 7 trailing zeros in 30!
```

**Verification:** 30! = 265,252,859,812,191,058,636,308,480,000,000
Count the zeros: 7 trailing zeros ✓

### Complexity Analysis
- Time: O(log₅ n) - we divide by increasing powers of 5
- Space: O(1) - only storing count
- Much better than O(n) or trying to calculate factorial!

### Key Insight
This is a perfect example of mathematical thinking in DSA:
1. Don't compute what you can deduce
2. Find the pattern/formula
3. Use mathematical properties (prime factorization)
4. Avoid overflow and inefficiency

**Remember:** You're counting 5s, not computing factorials!

---

## 6. Prime Factorization

### What is it?
Prime factorization is expressing a number as a product of prime numbers.

**Prime Number:** A number greater than 1 that has no positive divisors other than 1 and itself.
Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23...

**Examples of Prime Factorization:**
- 12 = 2 × 2 × 3 = 2² × 3
- 100 = 2 × 2 × 5 × 5 = 2² × 5²
- 315 = 3 × 3 × 5 × 7 = 3² × 5 × 7
- 97 = 97 (already prime)

### Fundamental Theorem of Arithmetic
Every integer greater than 1 can be represented uniquely as a product of prime numbers (ignoring order).

This means:
- Prime factorization is UNIQUE
- 12 can ONLY be factored as 2² × 3
- No other combination of primes gives 12

### The Logic

**Basic Approach:**
1. Start with the smallest prime (2)
2. Divide the number by 2 as many times as possible
3. Move to the next prime (3, 5, 7, ...)
4. Continue until the number becomes 1

**Why start with smallest primes?**
- Efficiency: smaller primes divide more numbers
- Systematic: ensures we don't miss any factors
- Complete: eventually reduces number to 1

### Optimization: Check Only Up to √n

**Why this works:**
If n has a factor greater than √n, it MUST have a corresponding factor less than √n.

**Proof by example:**
- Take 100 (√100 = 10)
- Factors: 1, 2, 4, 5, 10, 20, 25, 50, 100
- Pairs: (1,100), (2,50), (4,25), (5,20), (10,10)
- Notice: one element of each pair is ≤ 10

So after checking up to √n:
- If nothing divided it, n itself is prime
- If something divided it, we found all factors

### Step-by-Step Example: 315

```
Start with 315

Check 2: 315 ÷ 2? No (315 is odd)

Check 3: 315 ÷ 3 = 105 ✓ [Factor: 3]
         105 ÷ 3 = 35 ✓  [Factor: 3]
         35 ÷ 3? No

Check 5: 35 ÷ 5 = 7 ✓ [Factor: 5]
         7 ÷ 5? No

Check 7: 7 ÷ 7 = 1 ✓ [Factor: 7]

Prime factors: 3, 3, 5, 7 → 315 = 3² × 5 × 7
```

### Why Skip Even Numbers After 2?
- 2 is the only even prime
- All other even numbers are divisible by 2
- So after checking 2, only check odd numbers: 3, 5, 7, 9, 11...
- This cuts work in half!

### Visual Representation (Factor Tree for 100)

```
         100
        /   \
       2    50
           /  \
          2   25
              / \
             5   5

Prime factors: 2, 2, 5, 5
```

### Complexity Analysis
- Time: O(√n) - checking divisors up to square root
- Space: O(1) - only storing factors
- Much better than checking all numbers up to n: O(n)

### Special Cases
- **n = 1**: No prime factors (by convention)
- **n is prime**: The only prime factor is n itself
- **n = 2**: Smallest prime, handle separately

### Applications in DSA
- GCD/LCM calculations
- Cryptography (RSA algorithm)
- Checking if numbers are coprime
- Simplifying fractions
- Many number theory problems

### Key Insight
Prime factorization is fundamental because:
1. Every number is built from primes (building blocks)
2. Unique representation helps in comparisons
3. Many problems reduce to prime analysis
4. √n optimization is crucial for efficiency

---

## 7. All Divisors of a Number

### What is it?
Divisors (also called factors) are numbers that divide a given number completely (no remainder).

**Examples:**
- Divisors of 12: 1, 2, 3, 4, 6, 12
- Divisors of 20: 1, 2, 4, 5, 10, 20
- Divisors of 100: 1, 2, 4, 5, 10, 20, 25, 50, 100
- Divisors of 7: 1, 7 (prime numbers have exactly 2 divisors)

### Properties of Divisors
1. **1 and n**: Every number n has at least two divisors: 1 and itself
2. **Symmetric pairs**: Divisors come in pairs that multiply to n
3. **Odd count**: Perfect squares have an odd number of divisors

### The Naive Approach
Check every number from 1 to n:
- Test if each divides n evenly
- If yes, it's a divisor
- Time: O(n) - very slow for large numbers

**Example for 100:**
Check: 1? Yes. 2? Yes. 3? No. 4? Yes. 5? Yes. ... 99? No. 100? Yes.

### The Brilliant Insight: Pair Property

**Key observation:** Divisors come in pairs!

If `i` divides `n`, then `n/i` also divides `n`.

**Example for 100:**
```
1 × 100 = 100  → (1, 100) both are divisors
2 × 50 = 100   → (2, 50) both are divisors
4 × 25 = 100   → (4, 25) both are divisors
5 × 20 = 100   → (5, 20) both are divisors
10 × 10 = 100  → (10, 10) both are divisors
```

**Pattern:** One number in each pair is ≤ √100 = 10

### Optimized Approach: Check Only Up to √n

**Logic:**
1. Check numbers only from 1 to √n
2. For each divisor i found, also add n/i
3. Special case: if i = √n (perfect square), add it only once

**Why this works:**
- All divisor pairs have one element ≤ √n
- By finding one, we automatically know the other
- Reduces checking from n numbers to √n numbers

### Step-by-Step Example: Finding divisors of 36

```
√36 = 6, so check 1 to 6

Check 1: 36 ÷ 1 = 36 ✓ → Add both: 1, 36
Check 2: 36 ÷ 2 = 18 ✓ → Add both: 2, 18
Check 3: 36 ÷ 3 = 12 ✓ → Add both: 3, 12
Check 4: 36 ÷ 4 = 9 ✓  → Add both: 4, 9
Check 5: 36 ÷ 5? No
Check 6: 36 ÷ 6 = 6 ✓  → Add once: 6 (pair is same!)

Divisors: 1, 2, 3, 4, 6, 9, 12, 18, 36
```

### Perfect Squares: Special Handling

For perfect squares, √n is a divisor that pairs with itself:
- √36 = 6, and 6 × 6 = 36
- Don't count it twice!

**Examples:**
- 16 = 4 × 4 → divisors include 4 once
- 25 = 5 × 5 → divisors include 5 once
- 100 = 10 × 10 → divisors include 10 once

### Visualization for 100

```
Checking 1 to 10 (√100 = 10):

i=1:  100/1=100  → Add: 1, 100
i=2:  100/2=50   → Add: 2, 50
i=3:  100/3≈33.3 → Skip
i=4:  100/4=25   → Add: 4, 25
i=5:  100/5=20   → Add: 5, 20
i=6:  100/6≈16.7 → Skip
i=7:  100/7≈14.3 → Skip
i=8:  100/8=12.5 → Skip
i=9:  100/9≈11.1 → Skip
i=10: 100/10=10  → Add: 10 (once, since 10=10)

Result: 1, 2, 4, 5, 10, 20, 25, 50, 100
```

### Complexity Analysis

**Naive Approach:**
- Time: O(n)
- Space: O(1)
- Must check every single number

**Optimized Approach:**
- Time: O(√n)
- Space: O(number of divisors) to store them
- Massive improvement!

**Example comparison:**
- For n = 1,000,000:
  - Naive: 1,000,000 checks
  - Optimized: 1,000 checks (1000× faster!)

### How to Get Divisors in Sorted Order

The pair method gives divisors unsorted:
- As you find pairs, you get: 1, 100, 2, 50, 4, 25, 5, 20, 10

**To sort:**
- Store all divisors, then sort at end
- OR: Store divisors ≤ √n in one list, > √n in another (already sorted), then combine

### Relationship with Prime Factorization

If you know prime factorization, you can find number of divisors:

**Formula:** If n = p₁^a × p₂^b × p₃^c, then:
Number of divisors = (a+1) × (b+1) × (c+1)

**Example:** 100 = 2² × 5²
- Number of divisors = (2+1) × (2+1) = 3 × 3 = 9
- Count: 1, 2, 4, 5, 10, 20, 25, 50, 100 → 9 divisors ✓

### Key Insight

The pair property is powerful:
- Turns O(n) problem into O(√n)
- Used in many number theory problems
- **Remember:** When you find one divisor, you get two for free (except for perfect squares)
- Square root is your friend in optimization!

---

## 8. Sieve of Eratosthenes

### What is it?
An ancient algorithm to find ALL prime numbers up to a given number n efficiently.

Named after Eratosthenes of Cyrene, a Greek mathematician who lived around 200 BCE.

**Problem:** Given n, find all primes ≤ n.

**Examples:**
- Primes ≤ 10: 2, 3, 5, 7
- Primes ≤ 20: 2, 3, 5, 7, 11, 13, 17, 19
- Primes ≤ 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

### Why Do We Need This?

**The Naive Approach** (check each number individually):
- For each number from 2 to n
- Check if it's prime (test divisibility up to √number)
- Time: O(n × √n) - very slow!

**The Sieve Approach:**
- Find all primes at once
- Time: O(n log log n) - much faster!
- Especially efficient when you need multiple primes

### The Core Idea

Instead of checking each number, ELIMINATE non-primes:
1. Assume all numbers are prime initially
2. Starting from 2, mark all its multiples as non-prime
3. Move to next unmarked number, repeat
4. What remains unmarked → primes!

**Why this works:**
- Any composite (non-prime) number must have a prime factor ≤ √n
- By marking multiples of all primes up to √n, we eliminate all composites
- What survives the sieve must be prime!

### The Algorithm Step-by-Step

**Setup:**
- Create a list: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15...
- Mark all as "potentially prime"

**Process:**
1. Start with 2 (first prime)
2. Keep 2 as prime, mark all multiples of 2 as non-prime: 4, 6, 8, 10, 12, 14...
3. Move to next unmarked (3)
4. Keep 3 as prime, mark all multiples of 3 as non-prime: 6, 9, 12, 15, 18...
5. Move to next unmarked (5)
6. Keep 5 as prime, mark all multiples of 5 as non-prime: 10, 15, 20, 25, 30...
7. Continue until you reach √n

### Detailed Example: n = 30

```
Initial: 2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30

Process 2 (keep 2, mark its multiples):
         2  3  X  5  X  7  X  9  X   11  X   13  X   15  X   17  X   19  X   21  X   23  X   25  X   27  X   29  X

Process 3 (keep 3, mark its multiples):
         2  3  X  5  X  7  X  X  X   11  X   13  X   X   X   17  X   19  X   X   X   23  X   25  X   X   X   29  X

Process 5 (keep 5, mark its multiples):
         2  3  X  5  X  7  X  X  X   11  X   13  X   X   X   17  X   19  X   X   X   23  X   X   X   X   X   29  X

√30 ≈ 5.5, so we're done!

Primes (unmarked): 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
```

### Key Optimization: Start Marking from p²

When processing prime p, start marking from p² instead of 2p.

**Why?**
- All smaller multiples (2p, 3p, ..., (p-1)p) have already been marked!
- They were marked when we processed smaller primes

**Example with p=5:**
- 2×5 = 10 (already marked by 2)
- 3×5 = 15 (already marked by 3)
- 4×5 = 20 (already marked by 2)
- 5×5 = 25 (first new one to mark!)

### Why Stop at √n?

After processing all primes up to √n, all composites are marked.

**Reason:**
- Every composite number has a prime factor ≤ √n
- By eliminating multiples of all primes ≤ √n, we've eliminated all composites
- Anything remaining must be prime

**Example:** For n=100, √100=10
- Process primes: 2, 3, 5, 7 (all ≤ 10)
- This is sufficient to mark all composites up to 100!

### Visual Representation (n=50)

```
Start:    [2  3  4  5  6  7  8  9  10  11  12  13 ... 50]

After 2:  [2  3  ✗  5  ✗  7  ✗  9  ✗  11  ✗  13 ... ✗]
          (crossed out: 4,6,8,10,12,14,16,18,20...)

After 3:  [2  3  ✗  5  ✗  7  ✗  ✗  ✗  11  ✗  13 ... ✗]
          (crossed out: 9,15,21,27,33,39,45...)

After 5:  [2  3  ✗  5  ✗  7  ✗  ✗  ✗  11  ✗  13 ... ✗]
          (crossed out: 25,35,45...)

After 7:  [2  3  ✗  5  ✗  7  ✗  ✗  ✗  11  ✗  13 ... ✗]
          (crossed out: 49...)

√50 ≈ 7, stop here!

Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
```

### Complexity Analysis

**Time Complexity: O(n log log n)**
- This is nearly linear!
- Much better than O(n√n) naive approach
- One of the most efficient prime-finding algorithms

**Space Complexity: O(n)**
- Need array to store prime/not-prime status
- Trade space for time

**Performance Comparison:**
- Naive (checking each): ~10 seconds for n=1,000,000
- Sieve: ~0.1 seconds for n=1,000,000
- 100× faster!

### When to Use Sieve?

**Use Sieve when:**
- Need multiple primes (not just one)
- Need all primes in a range
- Range is not too large (< 10 million)
- Can afford O(n) space

**Don't use Sieve when:**
- Need just one prime check
- Range is huge (billions)
- Memory is limited
- Need primes in very large range (use segmented sieve)

### Variations

**Segmented Sieve:**
- For very large ranges
- Process in chunks
- Reduces space requirement

**Sieve of Atkin:**
- Alternative algorithm
- Slightly faster for large n
- More complex to implement

### Key Insight

The Sieve of Eratosthenes is a perfect example of:
- **Trade-off**: Space for time
- **Smart elimination**: Mark non-primes instead of checking each
- **Historical algorithm**: Still used after 2000+ years!
- **Batch processing**: Finding all primes together is faster than one-by-one

**Remember:** 
- It's a sieve (filter) that lets primes pass through
- Composite numbers get "caught" in the mesh
- Ancient wisdom meets modern efficiency!

---

## 9. Computing Power

### What is it?
Computing power means calculating x^n (x raised to the power n).

**Examples:**
- 2³ = 2 × 2 × 2 = 8
- 3⁴ = 3 × 3 × 3 × 3 = 81
- 5² = 5 × 5 = 25
- 10⁰ = 1 (any number to power 0 is 1)
- 2¹⁰ = 1024

### The Naive Approach

Simply multiply x with itself n times:
- Result = 1
- Multiply by x, then by x, then by x... (n times)
- Time: O(n) - need n multiplications

**Example: 2⁵**
```
Start: result = 1
Step 1: 1 × 2 = 2
Step 2: 2 × 2 = 4
Step 3: 4 × 2 = 8
Step 4: 8 × 2 = 16
Step 5: 16 × 2 = 32
```

**Problem:** For large n, this is very slow!
- 2¹⁰⁰⁰ would need 1000 multiplications

### The Brilliant Insight: Divide and Conquer

**Key observation:**
- If n is even: x^n = (x^(n/2))²
- If n is odd: x^n = x × (x^(n/2))²

**Why this is powerful:**
Instead of n multiplications, we can do log(n) multiplications!

**Example: 2¹⁰**
```
Naive way: 2×2×2×2×2×2×2×2×2×2 (10 multiplications)

Smart way:
2¹⁰ = (2⁵)²
2⁵ = 2 × (2²)²
2² = (2¹)²
2¹ = 2

Working backwards:
2¹ = 2
2² = 2 × 2 = 4
2⁵ = 2 × (4)² = 2 × 16 = 32
2¹⁰ = (32)² = 1024

Only 4 steps instead of 10!
```

### Recursive Approach Logic

**Base case:** 
- x⁰ = 1 (anything to power 0)

**Recursive cases:**
1. Calculate: temp = power(x, n/2)
2. If n is even: return temp × temp
3. If n is odd: return x × temp × temp

**Why calculate n/2 only once?**
- Instead of: power(x, n/2) × power(x, n/2)
- We do: temp = power(x, n/2), then temp × temp
- Avoids redundant calculations
- This is called "memoization" or caching

### Recursion Tree for 2⁸

```
                    2⁸
                     ↓
                  (2⁴)²
                     ↓
                  (2²)²
                     ↓
                  (2¹)²
                     ↓
                    2

Evaluating back up:
2¹ = 2
2² = 2² = 4
2⁴ = 4² = 16
2⁸ = 16² = 256
```

### Even vs Odd Powers

**For even powers:**
- No extra x needed
- Just square the result of n/2
- Example: 2⁸ = (2⁴)² = 16² = 256

**For odd powers:**
- Need to multiply by one extra x
- Square result of n/2, then multiply by x
- Example: 2⁷ = 2 × (2³)² = 2 × 8² = 2 × 64 = 128

**Why the extra x?**
- 2⁷ = 2 × 2⁶
- We can compute 2⁶ as (2³)²
- Then multiply by the leftover 2

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Naive Iterative | O(n) | O(1) | Simple but slow |
| Recursive (D&C) | O(log n) | O(log n) | Fast but uses stack |

**Why O(log n)?**
- Each recursion halves n
- Number of steps = how many times you can halve n until reaching 1
- That's exactly log₂(n)!

**Example:**
- n = 1024 = 2¹⁰
- Naive: 1024 steps
- Recursive: 10 steps (log₂(1024) = 10)
- 100× faster!

### Visual Example: 3¹³

```
3¹³ (odd)
 = 3 × (3⁶)²
 = 3 × 729² (where 3⁶=729)

3⁶ (even)
 = (3³)²
 = 27² = 729 (where 3³=27)

3³ (odd)
 = 3 × (3¹)²
 = 3 × 9 = 27 (where 3¹=3, 3²=9)

3¹ (base case)
 = 3

Building back:
3¹ = 3
3³ = 3 × 3² = 3 × 9 = 27
3⁶ = 27² = 729
3¹³ = 3 × 729² = 3 × 531,441 = 1,594,323
```

### Special Cases

**x⁰ = 1:** Any number (except 0) to power 0 is 1
**0⁰:** Undefined (mathematically controversial)
**x¹ = x:** Any number to power 1 is itself
**1ⁿ = 1:** One to any power is 1
**0ⁿ = 0:** Zero to any positive power is 0

### Negative Powers

For negative exponents: x⁻ⁿ = 1/(xⁿ)
- 2⁻³ = 1/(2³) = 1/8
- Can compute xⁿ, then take reciprocal

### Key Insight

**Divide and Conquer pattern:**
1. Break problem into smaller subproblems
2. Solve subproblems recursively
3. Combine results

**Power computation shows:**
- Simple problems can have clever optimizations
- Halving the problem size repeatedly → logarithmic time
- Trade stack space for speed (recursion uses call stack)
- Foundation for even more efficient iterative version (next topic!)

**Remember:** Don't multiply n times when you can halve and square!

---

## 10. Binary Exponentiation (Iterative Power)

### What is it?
The MOST efficient way to compute x^n, using binary representation of the exponent.

Also called:
- Fast exponentiation
- Exponentiation by squaring (iterative version)
- Russian peasant method for exponentiation

### The Core Insight: Binary Representation

Every number can be written in binary (base 2).

**Examples:**
- 13 = 8 + 4 + 1 = 2³ + 2² + 2⁰ = 1101₂
- 10 = 8 + 2 = 2³ + 2¹ = 1010₂
- 5 = 4 + 1 = 2² + 2⁰ = 101₂

**Key idea:** 
x¹³ = x^(8+4+1) = x⁸ × x⁴ × x¹

### The Beautiful Logic

Instead of recursion, we process n's binary representation bit by bit!

**Algorithm:**
1. Start with result = 1
2. Look at each bit of n (from right to left)
3. If bit is 1: multiply result by current power of x
4. Square x for the next bit (because next bit represents 2× the power)
5. Move to next bit (divide n by 2)
6. Repeat until n becomes 0

### Step-by-Step Example: 3¹³

**Binary representation of 13:**
13 = 1101₂ (reading right to left: 1, 0, 1, 1)

```
Initial: x = 3, n = 13, result = 1

Bit 0 (rightmost): n = 13 (binary: 1101)
  - Last bit is 1? Yes
  - result = result × x = 1 × 3 = 3
  - Square x: x = 3² = 9
  - Shift n right: n = 13 ÷ 2 = 6 (binary: 110)

Bit 1: n = 6 (binary: 110)
  - Last bit is 1? No (it's 0)
  - Don't multiply result (stays 3)
  - Square x: x = 9² = 81
  - Shift n right: n = 6 ÷ 2 = 3 (binary: 11)

Bit 2: n = 3 (binary: 11)
  - Last bit is 1? Yes
  - result = result × x = 3 × 81 = 243
  - Square x: x = 81² = 6561
  - Shift n right: n = 3 ÷ 2 = 1 (binary: 1)

Bit 3: n = 1 (binary: 1)
  - Last bit is 1? Yes
  - result = result × x = 243 × 6561 = 1,594,323
  - Square x: x = 6561² = ...
  - Shift n right: n = 1 ÷ 2 = 0

n = 0, stop!
Final result: 1,594,323 ✓ (which equals 3¹³)
```

### Why This Works: Mathematical Proof

13 in binary is 1101₂, meaning:
13 = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 1

Therefore:
3¹³ = 3^(8+4+1) = 3⁸ × 3⁴ × 3¹

Now trace what our algorithm does:
- Starts with result = 1
- Bit 0 (1): multiplies by 3¹, result = 3
- Bit 1 (0): skips, result stays 3
- Bit 2 (1): multiplies by 3⁴ (which is 81), result = 3 × 81 = 243 = 3⁵
- Bit 3 (1): multiplies by 3⁸ (which is 6561), result = 243 × 6561 = 3¹³

Perfect match! ✓

### Another Example: 2¹⁰

**Binary of 10: 1010₂ (bits: 0, 1, 0, 1)**

```
Initial: x = 2, n = 10, result = 1

Iteration 1: n = 10 (binary: 1010)
  - Last bit = 0 (even) → Don't multiply
  - x = 2² = 4
  - n = 5 (binary: 101)

Iteration 2: n = 5 (binary: 101)
  - Last bit = 1 (odd) → result = 1 × 4 = 4
  - x = 4² = 16
  - n = 2 (binary: 10)

Iteration 3: n = 2 (binary: 10)
  - Last bit = 0 (even) → Don't multiply
  - x = 16² = 256
  - n = 1 (binary: 1)

Iteration 4: n = 1 (binary: 1)
  - Last bit = 1 (odd) → result = 4 × 256 = 1024
  - x = 256² = ...
  - n = 0

Final: 1024 ✓ (which equals 2¹⁰)
```

### The Pattern: Squaring Doubles the Power

Notice the pattern of x values:

**For 2¹⁰:**
- Start: x = 2 = 2¹
- After 1st square: x = 4 = 2²
- After 2nd square: x = 16 = 2⁴
- After 3rd square: x = 256 = 2⁸

Each squaring doubles the exponent: 1 → 2 → 4 → 8

This perfectly matches the binary place values!

### Bit Operations Explained

**Check if last bit is 1:**
- n % 2 gives 0 (even) or 1 (odd)
- n % 2 == 1 means last bit is 1
- n % 2 == 0 means last bit is 0

**Right shift (divide by 2):**
- n // 2 removes the rightmost bit
- 1101₂ becomes 110₂
- 13 becomes 6

### Why This is Better Than Recursive Approach

| Aspect | Recursive | Iterative (Binary) |
|--------|-----------|-------------------|
| Time | O(log n) | O(log n) |
| Space | O(log n) stack | O(1) |
| Clarity | More intuitive | More clever |
| Efficiency | Good | Best |

**Key advantage:** No recursion stack!
- Uses only a few variables
- Constant space O(1)
- Slightly faster in practice (no function call overhead)

### Visual: Processing Bits Right to Left

```
For x^n where n = 13 = 1101₂

Read binary right to left:
    ↓   ↓   ↓   ↓
    1   1   0   1
    ↑   ↑   ↑   ↑
   2³  2²  2¹  2⁰
   ×   ×   skip ×
  
Build result by multiplying when bit = 1:
result = x^(2⁰) × x^(2²) × x^(2³)
       = x¹ × x⁴ × x⁸
       = x¹³
```

### Complexity Analysis

**Time Complexity: O(log n)**
- Process each bit of n exactly once
- Number of bits in n = ⌊log₂ n⌋ + 1
- Therefore: O(log n) iterations

**Space Complexity: O(1)**
- Only use: result, x, n variables
- No recursion stack
- Constant space!

**Example:** For n = 1,000,000
- Binary has ⌊log₂(1,000,000)⌋ + 1 ≈ 20 bits
- Only 20 iterations needed
- Compare to 1,000,000 multiplications in naive approach!

### Applications in Real World

**1. Cryptography:**
- RSA encryption uses modular exponentiation
- Computing (x^n) mod m efficiently
- Essential for secure communication

**2. Computer Graphics:**
- Matrix transformations
- Repeated transformations (like rotation n times)

**3. Competitive Programming:**
- Required for many number theory problems
- Computing large powers modulo a prime
- Fibonacci numbers using matrix exponentiation

**4. Scientific Computing:**
- Numerical analysis
- Physics simulations
- Financial modeling

### Extension: Modular Exponentiation

Often we need (x^n) mod m (remainder when divided by m).

**Same algorithm, just add modulo:**
- After every multiplication: result = (result × x) % m
- After every square: x = (x × x) % m
- Prevents overflow and keeps numbers manageable

**Example:** Compute 7¹⁰ mod 13
- Instead of calculating 282,475,249 then taking mod
- Keep result small at each step
- Much more efficient!

### The Russian Peasant Connection

This method is similar to ancient Russian peasant multiplication:
- Halve one number, double the other
- Add up rows where first number is odd
- Same idea: using binary decomposition!

### Key Insight

Binary exponentiation is a masterpiece of algorithmic thinking:

1. **Use number representation:** Binary structure of exponent
2. **Eliminate redundancy:** Each square serves multiple purposes
3. **Bit-level processing:** Work with number's internal structure
4. **Optimal complexity:** Can't do better than O(log n)
5. **Space efficiency:** Iterative beats recursive

**Remember:**
- Every algorithm improvement comes from deeper understanding
- Binary representation unlocks many optimizations
- The iterative version is the gold standard for power computation
- Essential tool in competitive programming and cryptography

**The beauty:** A simple problem (multiply n times) becomes elegant when we understand the binary nature of numbers!

---

## Summary: Key Takeaways

### Mathematical Thinking in DSA

1. **Formulas beat brute force** - Always look for mathematical shortcuts
2. **√n is your friend** - Many optimizations involve checking only up to square root
3. **Don't compute what you can deduce** - Trailing zeros, prime properties, etc.
4. **Binary representation** - Understanding bits unlocks O(log n) solutions
5. **Pair properties** - Symmetric relationships reduce work by half

### Complexity Patterns

| Pattern | Time | Example |
|---------|------|---------|
| Direct Formula | O(1) | Sum of n numbers |
| Digit Processing | O(d) | Count digits, palindrome |
| Up to √n | O(√n) | Prime factors, divisors |
| Halving | O(log n) | Binary exponentiation, trailing zeros |
| Sieve | O(n log log n) | Multiple primes |

### Problem-Solving Approach

1. **Understand the problem** - What's really being asked?
2. **Look for patterns** - Mathematical properties, symmetries
3. **Start simple** - Brute force first to understand
4. **Optimize** - Apply mathematical insights
5. **Verify** - Test with examples

### Essential Tricks

- **Digit extraction:** n % 10 (last digit), n // 10 (remove last digit)
- **Prime checking:** Test divisors up to √n only
- **Pair finding:** If i divides n, so does n/i
- **Binary thinking:** Process bits for logarithmic solutions
- **Modulo arithmetic:** Keep numbers small in calculations

---