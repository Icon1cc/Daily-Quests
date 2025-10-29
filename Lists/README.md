# Python Lists - Complete Theory Guide

## Table of Contents
1. [Introduction to Lists](#1-introduction-to-lists)
2. [Average of a List](#2-average-of-a-list)
3. [Separate Even and Odd Numbers](#3-separate-even-and-odd-numbers)
4. [Get Smaller Elements](#4-get-smaller-elements)
5. [Slicing](#5-slicing)
6. [Comprehensions](#6-comprehensions)
7. [Largest Element](#7-largest-element)
8. [Second Largest Element](#8-second-largest-element)
9. [Check if List is Sorted](#9-check-if-list-is-sorted)
10. [Reverse a List](#10-reverse-a-list)
11. [Remove Duplicates](#11-remove-duplicates)
12. [Left Rotate by One](#12-left-rotate-by-one)
13. [One Odd Occurring](#13-one-odd-occurring)

---

## 1. Introduction to Lists

### Theory
- Lists are **mutable**, ordered collections that can hold elements of different data types
- Elements are enclosed in square brackets `[]` and separated by commas
- Lists support indexing (positive and negative) and various operations

### Key Characteristics
- **Dynamic sizing**: Lists can grow or shrink
- **Heterogeneous**: Can contain integers, strings, objects, etc.
- **Mutable**: Elements can be modified after creation
- **Ordered**: Elements maintain insertion order

### Basic Operations
- **Creating**: `List = [1, 2, 3]`
- **Accessing**: `List[0]` (returns first element)
- **Negative Indexing**: `List[-1]` (returns last element)

### Important Methods
| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `append(x)` | Add element at end | O(1) |
| `insert(i, x)` | Insert at position i | O(n) |
| `extend(iterable)` | Add multiple elements | O(k) where k is length of iterable |
| `remove(x)` | Remove first occurrence | O(n) |
| `pop()` | Remove last element | O(1) |
| `pop(i)` | Remove element at index i | O(n) |

---

## 2. Average of a List

### Theory
Average = Sum of all elements ÷ Number of elements

### Logic Approach

**Method 1: Using Built-in Functions**
- Use `sum()` to get the total sum
- Use `len()` to get the count of elements
- Divide sum by length

**Method 2: Iterative Approach**
- Initialize `sum_of_list = 0`
- Iterate through each element and add to sum
- Divide by length of list

### Complexity Analysis
- **Time Complexity**: O(n) - Must visit each element once
- **Space Complexity**: O(1) - Only storing sum and average

### When to Use
- Data analysis and statistics
- Finding mean values in datasets
- Performance metrics calculation

---

## 3. Separate Even and Odd Numbers

### Theory
Split a list into two separate lists based on whether numbers are divisible by 2

### Logic Approach
1. Create two empty lists: `even = []` and `odd = []`
2. Iterate through the original list
3. For each element `x`:
   - If `x % 2 == 0`: append to `even` list
   - Else: append to `odd` list
4. Return both lists

### Key Concept
- **Modulo operator (%)**: Returns remainder of division
- `x % 2 == 0` → x is even
- `x % 2 != 0` → x is odd

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass through list
- **Space Complexity**: O(n) - Storing elements in two new lists

### Variations
Can extend this logic to separate by any condition:
- Divisible by 3, 5, etc.
- Positive vs negative numbers
- Prime vs composite

---

## 4. Get Smaller Elements

### Theory
Return all elements from a list that are less than a given value `x`

### Logic Approach
1. Initialize empty result list `res = []`
2. Iterate through each element `e` in list
3. If `e < x`: append to result list
4. Return result list

### Key Concept
- **Filtering**: Selecting elements based on a condition
- Can be done with loops or list comprehension

### Complexity Analysis
- **Time Complexity**: O(n) - Must check each element
- **Space Complexity**: O(k) - Where k is number of elements less than x

### Real-world Applications
- Filtering data below threshold
- Finding values in range
- Database query operations

---

## 5. Slicing

### Theory
Slicing extracts a portion of a sequence using the syntax: `sequence[start:stop:step]`

### Parameters
- **start**: Index where slice begins (inclusive). Default = 0
- **stop**: Index where slice ends (exclusive). Default = len(sequence)
- **step**: Increment between indices. Default = 1

### Important Slicing Patterns

| Syntax | Meaning | Example with `[10,20,30,40,50]` |
|--------|---------|----------------------------------|
| `l[:]` | Full copy | `[10,20,30,40,50]` |
| `l[2:]` | From index 2 to end | `[30,40,50]` |
| `l[:3]` | From start to index 3 | `[10,20,30]` |
| `l[1:4]` | From index 1 to 4 | `[20,30,40]` |
| `l[::2]` | Every 2nd element | `[10,30,50]` |
| `l[::-1]` | Reverse the list | `[50,40,30,20,10]` |
| `l[-3:]` | Last 3 elements | `[30,40,50]` |

### Logic for Negative Indices
- `-1` refers to last element
- `-2` refers to second-last element
- Works backwards from the end

### Complexity Analysis
- **Time Complexity**: O(k) - Where k is the length of the slice
- **Space Complexity**: O(k) - Creates new list with k elements

### Key Differences

**Lists vs Tuples/Strings**:
- Slicing a **list** creates a new list (different object)
- Slicing a **tuple** or **string** may return the same object (if slice is entire sequence)
  - Because tuples and strings are immutable
  - Python optimizes by reusing the same object

---

## 6. Comprehensions

### Theory
Comprehensions provide a concise way to create sequences from existing sequences

### 6.1 List Comprehension

**Syntax**: `[expression for item in iterable if condition]`

**Logic**:
1. Iterate through each item in iterable
2. Apply condition (optional)
3. If condition is true, evaluate expression
4. Add result to new list

**Examples**:
```python
# Get even numbers
evens = [x for x in list if x % 2 == 0]

# Square all numbers
squares = [x**2 for x in list]

# Conditional transformation
result = [x*2 if x > 5 else x for x in list]
```

**Complexity**: O(n) time, O(n) space

---

### 6.2 Dictionary Comprehension

**Syntax**: `{key: value for item in iterable if condition}`

**Logic**:
1. Iterate through iterable
2. Generate key-value pairs
3. Apply condition (optional)
4. Build dictionary

**Common Use Cases**:
- Creating mappings: `{x: x**3 for x in list}`
- Inverting dictionaries: `{v: k for k, v in dict.items()}`
- Filtering: `{k: v for k, v in dict.items() if condition}`

**Alternative**: `dict(zip(keys, values))`

**Complexity**: O(n) time, O(n) space

---

### 6.3 Set Comprehension

**Syntax**: `{expression for item in iterable if condition}`

**Logic**: Same as list comprehension but uses `{}` and automatically removes duplicates

**Key Feature**: Automatically handles duplicates (only unique values stored)

**Example**: `{x for x in list if x % 2 == 0}` → Only unique even numbers

**Complexity**: O(n) time, O(k) space (k = unique elements)

---

### 6.4 Generator Comprehension

**Syntax**: `(expression for item in iterable if condition)`

**Key Differences from List Comprehension**:
- Uses parentheses `()` instead of square brackets
- **Lazy evaluation**: Generates values on-the-fly
- **Memory efficient**: Doesn't store entire list in memory
- Returns a generator object (iterable)

**When to Use**:
- Large datasets where you don't need all values at once
- When processing one item at a time
- Memory-constrained environments

**Example**:
```python
gen = (x**2 for x in range(1000000))  # Doesn't create million-element list
for val in gen:  # Values generated as needed
    print(val)
```

**Complexity**: O(1) space (generates on demand)

---

## 7. Largest Element in a List

### Theory
Find the maximum element in a list of numbers

### Logic Approaches

**Method 1: Naive Solution (Nested Loops)**
1. For each element `x`:
   - Compare with every other element `y`
   - If any `y > x`, `x` is not the largest
   - If no element is greater, `x` is the largest
2. Return that element

**Complexity**: 
- Time: O(n²) - Nested loops
- Space: O(1)

---

**Method 2: Single Pass (Efficient)**
1. Assume first element `l[0]` is the maximum
2. Iterate from index 1 to end
3. For each element:
   - If element > current max: update max
4. Return maximum

**Logic**:
```
res = l[0]
for i in range(1, len(l)):
    if l[i] > res:
        res = l[i]
```

**Why This Works**:
- By the time we finish, `res` has been compared with every element
- Any element greater than `res` would have updated it
- Therefore, `res` holds the maximum

**Complexity**: 
- Time: O(n) - Single pass
- Space: O(1) - Only one variable

---

**Method 3: Built-in Function**
Use `max(list)` function

**Complexity**: O(n) time, O(1) space

---

## 8. Second Largest Element in a List

### Theory
Find the element that is second in order of magnitude (not second position)

### Edge Cases
- List with less than 2 elements → Return None
- All elements same → No second largest exists
- Only two distinct values → Second is the smaller one

### Logic Approaches

**Method 1: Two-Pass Approach**
1. **First Pass**: Find the largest element
2. **Second Pass**: Find largest element excluding the previous largest

**Algorithm**:
```
1. largest = max(list)
2. second_largest = None
3. For each element x in list:
   - If x != largest:
     - If second_largest is None OR x > second_largest:
       - second_largest = x
4. Return second_largest
```

**Complexity**: 
- Time: O(n) - Two separate passes
- Space: O(1)

---

**Method 2: Single-Pass Approach (Optimal)**
1. Initialize `largest = l[0]` and `second_largest = None`
2. For each element from index 1:
   - **If element > largest**:
     - `second_largest = largest` (old largest becomes second)
     - `largest = element` (new largest)
   - **Else if element != largest**:
     - If `second_largest is None` OR `element > second_largest`:
       - `second_largest = element`
3. Return second_largest

**Why This Works**:
- We always maintain the top 2 values
- When we find a new largest, the old largest becomes second
- When we find a value between largest and second, we update second

**Complexity**: 
- Time: O(n) - Single pass
- Space: O(1)

**Important**: Must check `x != largest` to avoid duplicates of largest being considered as second

---

## 9. Check if List is Sorted

### Theory
Determine if a list is in ascending order (equal consecutive values allowed)

### Logic Approaches

**Method 1: Using Built-in**
1. Create sorted copy: `sorted_list = sorted(original_list)`
2. Compare: `original_list == sorted_list`
3. If equal → sorted, else → not sorted

**Complexity**: 
- Time: O(n log n) - Sorting operation
- Space: O(n) - Creating sorted copy

---

**Method 2: Iterative Check (Optimal)**
**Algorithm**:
```
1. Start from index 1
2. For each element at index i:
   - Compare with previous element at i-1
   - If l[i] < l[i-1]: return False (not sorted)
3. If loop completes: return True (sorted)
```

**Logic**:
- In a sorted list, each element should be ≥ previous element
- If we find any element smaller than previous → list is not sorted
- If we check all adjacent pairs without finding violation → list is sorted

**Complexity**: 
- Time: O(n) - Single pass
- Space: O(1) - No extra space

**Why Optimal**: Stops immediately when unsorted pair found (early termination)

---

## 10. Reverse a List

### Theory
Reverse the order of elements in a list

### Logic Approaches

**Method 1: Built-in Methods**

a) **In-place reversal**: `list.reverse()`
   - Modifies original list
   - Returns None

b) **New reversed list**: `new_list = list(reversed(list))`
   - Creates new list
   - Original unchanged

c) **Slicing**: `new_list = list[::-1]`
   - Creates new list
   - Uses negative step to traverse backwards

**Complexity (all)**: O(n) time, O(1) or O(n) space depending on method

---

**Method 2: Append/Pop**
```
l.append(l.pop(0))  # Repeated n-1 times for full reversal
```
- `pop(0)` removes first element
- `append()` adds it to end
- Repeat for all elements

**Complexity**: 
- Time: O(n²) - pop(0) is O(n), done n times
- Not efficient!

---

**Method 3: Two-Pointer Approach (Optimal for in-place)**

**Algorithm**:
```
1. Initialize: left = 0, right = len(list) - 1
2. While left < right:
   - Swap list[left] and list[right]
   - left += 1
   - right -= 1
```

**Logic**:
- Start from both ends
- Swap elements and move pointers toward center
- Stop when pointers meet or cross

**Visual Example**: `[10, 20, 30, 40]`
```
Step 1: [10, 20, 30, 40]  left=0, right=3
        Swap: [40, 20, 30, 10]
        
Step 2: [40, 20, 30, 10]  left=1, right=2
        Swap: [40, 30, 20, 10]
        
Step 3: left=2, right=1 → Stop (left >= right)
```

**Complexity**: 
- Time: O(n) - Each element swapped once
- Space: O(1) - Only two pointers

---

## 11. Remove Duplicates

### Theory
Remove duplicate elements from a **sorted** array and return new size

### Key Insight
Since array is sorted, duplicates are adjacent! This makes it easier.

### Logic Approaches

**Method 1: Using Extra Space**

**Algorithm**:
```
1. Create temp array of same size
2. temp[0] = arr[0]  (first element always unique)
3. res = 1  (count of unique elements)
4. For i from 1 to n:
   - If temp[res-1] != arr[i]:  (current element different from last unique)
     - temp[res] = arr[i]
     - res += 1
5. Copy temp back to arr
6. Return res
```

**Logic**:
- Keep only elements that differ from the last stored unique element
- Since array is sorted, this ensures no duplicates

**Example**: `[10, 20, 20, 30, 30, 30]`
```
temp[0] = 10, res = 1
i=1: 20 != 10 → temp[1] = 20, res = 2
i=2: 20 == 20 → skip
i=3: 30 != 20 → temp[2] = 30, res = 3
i=4: 30 == 30 → skip
i=5: 30 == 30 → skip
Result: [10, 20, 30], res = 3
```

**Complexity**: 
- Time: O(n)
- Space: O(n) - Extra array

---

**Method 2: In-place (Constant Space) - Optimal**

**Algorithm**:
```
1. res = 1  (position to place next unique element)
2. For i from 1 to n:
   - If arr[res-1] != arr[i]:  (found new unique element)
     - arr[res] = arr[i]
     - res += 1
3. Return res
```

**Logic**:
- Use `res` to track position for next unique element
- Compare current with last unique element at `arr[res-1]`
- If different, place at position `res` and increment
- Elements beyond `res` are discarded

**Example**: `[10, 20, 20, 30, 30]`
```
arr = [10, 20, 20, 30, 30], res = 1

i=1: arr[0]=10 != arr[1]=20 → arr[1]=20, res=2
i=2: arr[1]=20 == arr[2]=20 → skip
i=3: arr[1]=20 != arr[3]=30 → arr[2]=30, res=3
i=4: arr[2]=30 == arr[4]=30 → skip

Final: [10, 20, 30, 30, 30], return 3
       (first 3 elements are unique)
```

**Complexity**: 
- Time: O(n) - Single pass
- Space: O(1) - In-place

**Why This Works**:
- Reading pointer (i) always ahead of writing pointer (res)
- We never overwrite unprocessed elements
- Sorted property ensures duplicates are consecutive

---

## 12. Left Rotate by One

### Theory
Move all elements one position to the left, first element goes to last position

**Example**: `[10, 20, 30, 40]` → `[20, 30, 40, 10]`

### Logic Approaches

**Method 1: Slicing**
```python
l = l[1:] + l[0:1]
```
- `l[1:]` → All elements except first: `[20, 30, 40]`
- `l[0:1]` → First element as list: `[10]`
- Concatenate: `[20, 30, 40, 10]`

**Complexity**: 
- Time: O(n) - Creating new list
- Space: O(n) - New list created

---

**Method 2: Pop and Append**
```python
l.append(l.pop(0))
```
- `pop(0)` removes and returns first element
- `append()` adds it to end

**Complexity**: 
- Time: O(n) - pop(0) shifts all elements
- Space: O(1) - In-place

---

**Method 3: Iterative Shift (Optimal)**

**Algorithm**:
```
1. Store first element: temp = l[0]
2. For i from 1 to n-1:
   - l[i-1] = l[i]  (shift each element left)
3. l[n-1] = temp  (place first element at end)
```

**Logic**:
```
Initial: [10, 20, 30, 40]
temp = 10

i=1: l[0] = l[1] → [20, 20, 30, 40]
i=2: l[1] = l[2] → [20, 30, 30, 40]
i=3: l[2] = l[3] → [20, 30, 40, 40]

l[3] = temp → [20, 30, 40, 10]
```

**Complexity**: 
- Time: O(n) - Single pass
- Space: O(1) - Only one temporary variable

**Why Optimal**: True in-place operation with minimal operations

---

## 13. One Odd Occurring

### Theory
In an array where all numbers appear an even number of times except one number that appears an odd number of times, find that number.

**Example**: `[4, 3, 4, 4, 4, 5, 5, 3, 3]`
- 4 appears 4 times (even)
- 5 appears 2 times (even)
- 3 appears 3 times (odd) ← Answer

### Logic Approaches

**Method 1: Brute Force (Nested Loops)**

**Algorithm**:
```
1. For each element i in array:
   - count = 0
   - For each element j in array:
     - If i == j: count += 1
   - If count % 2 != 0: return i
```

**Complexity**: 
- Time: O(n²) - Nested loops
- Space: O(1)

---

**Method 2: XOR Operation (Optimal)**

**Key Properties of XOR (^)**:
1. `x ^ 0 = x` (XOR with 0 returns the number itself)
2. `x ^ x = 0` (XOR of a number with itself is 0)
3. `x ^ y = y ^ x` (Commutative)
4. `(x ^ y) ^ z = x ^ (y ^ z)` (Associative)

**Algorithm**:
```
1. result = 0
2. For each element in array:
   - result = result ^ element
3. Return result
```

**How It Works**:

**Example**: `[4, 3, 4, 4, 4, 5, 5, 3, 3]`

```
result = 0
result = 0 ^ 4 = 4
result = 4 ^ 3 = 7
result = 7 ^ 4 = 3
result = 3 ^ 4 = 7
result = 7 ^ 4 = 3
result = 3 ^ 5 = 6
result = 6 ^ 5 = 3
result = 3 ^ 3 = 0
result = 0 ^ 3 = 3  ← Answer
```

**Why This Works**:
- All numbers occurring even times will cancel out (due to `x ^ x = 0`)
- Only the odd-occurring number remains
- Order doesn't matter due to associativity and commutativity

**Mathematical Proof**:
```
[4, 4, 4, 4, 3, 3, 3, 5, 5]
= (4 ^ 4) ^ (4 ^ 4) ^ (3 ^ 3) ^ 3 ^ (5 ^ 5)
= 0 ^ 0 ^ 0 ^ 3 ^ 0
= 3
```

**Complexity**: 
- Time: O(n) - Single pass
- Space: O(1) - Only one variable

**Why Optimal**: 
- Linear time complexity
- Constant space
- Elegant solution using bit manipulation

---

## Summary: When to Use Each Approach

| Problem | Optimal Approach | Time | Space | Key Insight |
|---------|------------------|------|-------|-------------|
| Average | Built-in sum()/len() | O(n) | O(1) | Simple aggregation |
| Even/Odd Split | Single pass with condition | O(n) | O(n) | Modulo operator |
| Get Smaller | Filter with condition | O(n) | O(k) | Linear search |
| Slicing | Built-in slicing | O(k) | O(k) | Creates new sequence |
| Comprehensions | List/Dict/Set/Generator | O(n) | Varies | Concise syntax |
| Largest | Single pass comparison | O(n) | O(1) | Track maximum |
| Second Largest | Single pass, two variables | O(n) | O(1) | Track top 2 |
| Is Sorted | Adjacent pair comparison | O(n) | O(1) | Early termination |
| Reverse | Two-pointer swap | O(n) | O(1) | In-place swapping |
| Remove Duplicates | Two pointers (sorted) | O(n) | O(1) | Leverage sorted property |
| Left Rotate | Iterative shift | O(n) | O(1) | Store and shift |
| Odd Occurring | XOR operation | O(n) | O(1) | Bit manipulation |

---

## Key Takeaways

1. **Choose the right tool**: Built-in functions are often optimized, but understanding algorithms is crucial

2. **Space-time tradeoffs**: Sometimes using extra space can improve time complexity

3. **In-place vs New structure**: Decide based on whether you need to preserve original data

4. **Early termination**: Exit loops as soon as answer is found (e.g., checking if sorted)

5. **Bit manipulation**: XOR is powerful for problems involving pairs/duplicates

6. **Two-pointer technique**: Effective for reversing, removing duplicates, and more

7. **List comprehensions**: More Pythonic and often faster than explicit loops

8. **Understand complexity**: Always analyze both time and space complexity

---

## Practice Strategy

1. **Understand the problem** thoroughly before coding
2. **Think of brute force** solution first
3. **Optimize** by identifying patterns and redundancies
4. **Analyze complexity** of your solution
5. **Code** the optimal solution
6. **Test** with edge cases (empty list, single element, duplicates)

