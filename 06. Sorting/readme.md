# Sorting Algorithms - Complete Reference Guide

## Table of Contents
1. [Bubble Sort](#bubble-sort) - [Code: Bubble Sort.py](./3.%20Bubble%20Sort.py)
2. [Bubble Sort Optimised](#bubble-sort-optimised) - [Code: Bubble Sort Optimised.py](./4.%20Bubble%20Sort%20Optimised.py)
3. [Selection Sort](#selection-sort) - [Code: Selection Sort.py](./5.%20Selection%20Sort.py)
4. [Insertion Sort](#insertion-sort) - [Code: Insertion Sort.py](./6.%20Insertion%20Sort.py)
5. [Merge Sort](#merge-sort) - [Code: Merging two sorted arrays.py](./7.%20Merging%20two%20sorted%20arrays.py), [Merge Subarrays.py](./8.%20Merge%20Subarrays.py), [Merge Sort.py](./9.%20Merge%20Sort.py)
6. [Quick Sort](#quick-sort) - [Code: Lomuto's Partition.py](./14.%20Lomuto's%20Partition.py), [Hoarse's Partition.py](./15.%20Hoarse's%20Partition.py), [QuickSort using Lomuto.py](./16.%20QuickSort%20using%20Lomuto.py), [QuickSort using Hoarse.py](./17.%20QuickSort%20using%20Hoarse.py)
7. [Heap Sort](#heap-sort) - [Code: Heap Sort.py](./18.%20Heap%20Sort.py)
8. [Additional Operations](#additional-operations)
9. [Comparison Summary](#comparison-summary)

---

## Bubble Sort
**📁 Implementation:** [3. Bubble Sort.py](./3.%20Bubble%20Sort.py)

### Logic
Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order. This process is repeated until the list is sorted. The largest element "bubbles up" to its correct position in each pass.

### How It Works
1. Compare adjacent elements starting from the beginning
2. If the left element is greater than the right, swap them
3. Move to the next pair and repeat
4. After each complete pass, the largest unsorted element is in its final position
5. Repeat for remaining unsorted portion until no swaps are needed

### Optimized Version
The optimized version tracks whether any swaps occurred in a pass. If no swaps happen, the array is already sorted and the algorithm terminates early.

### Time Complexity

| Case | Complexity | Calculation |
|------|------------|-------------|
| **Best Case** | O(n) | When array is already sorted. Only one pass needed with optimization. Comparisons: n-1 |
| **Average Case** | O(n²) | Random order. Passes: n-1, Comparisons per pass decrease: (n-1) + (n-2) + ... + 1 = n(n-1)/2 |
| **Worst Case** | O(n²) | Array sorted in reverse order. Maximum swaps needed. Total operations: n(n-1)/2 ≈ n²/2 |

### Space Complexity
- **Auxiliary Space**: O(1) - Only uses a few variables for swapping and loop control (in-place sorting)

### When to Use
- Small datasets (n < 50)
- Nearly sorted data (with optimization)
- Educational purposes
- When simplicity matters more than efficiency

---

## Bubble Sort Optimised
**📁 Implementation:** [4. Bubble Sort Optimised.py](./4.%20Bubble%20Sort%20Optimised.py)

### Logic
The optimized version of Bubble Sort adds a flag to track whether any swaps occurred during a pass. If no swaps happen in a complete pass, the array is already sorted and the algorithm can terminate early, avoiding unnecessary iterations.

### Logic
Selection Sort divides the array into sorted and unsorted regions. It repeatedly finds the minimum element from the unsorted region and places it at the end of the sorted region.

### How It Works
1. Start with the entire array as unsorted
2. Find the minimum element in the unsorted portion
3. Swap it with the first element of the unsorted portion
4. Move the boundary between sorted and unsorted one position right
5. Repeat until the entire array is sorted

### Time Complexity

| Case | Complexity | Calculation |
|------|------------|-------------|
| **Best Case** | O(n²) | Even if sorted, still searches entire unsorted portion each time. Comparisons: (n-1) + (n-2) + ... + 1 = n(n-1)/2 |
| **Average Case** | O(n²) | Always performs same number of comparisons regardless of input |
| **Worst Case** | O(n²) | Same as average case. Total comparisons: n(n-1)/2 |

### Space Complexity
- **Auxiliary Space**: O(1) - Only uses variables for index tracking and temporary storage (in-place sorting)

### Key Characteristic
- **Minimum number of swaps**: At most n-1 swaps (one per element), making it useful when write operations are expensive

### When to Use
- When memory writes are costly (flash memory, EEPROM)
- Small datasets
- When you need minimal number of swaps

---

## Insertion Sort
**📁 Implementation:** [6. Insertion Sort.py](./6.%20Insertion%20Sort.py)

### Logic
Insertion Sort builds the final sorted array one element at a time. It picks each element and inserts it into its correct position among the previously sorted elements, similar to sorting playing cards in your hand.

### How It Works
1. Start with the second element (first element is trivially sorted)
2. Compare it with elements in the sorted portion (to its left)
3. Shift all larger elements one position to the right
4. Insert the current element in its correct position
5. Repeat for all remaining elements

### Time Complexity

| Case | Complexity | Calculation |
|------|------------|-------------|
| **Best Case** | O(n) | Array already sorted. Each element compared once with previous: n-1 comparisons total |
| **Average Case** | O(n²) | Random order. On average, each element compared with half the sorted portion: 1 + 2 + 3 + ... + (n-1) ≈ n²/4 |
| **Worst Case** | O(n²) | Reverse sorted array. Each element compared with all previous elements: 1 + 2 + 3 + ... + (n-1) = n(n-1)/2 |

### Space Complexity
- **Auxiliary Space**: O(1) - Uses only a single variable to hold the element being inserted (in-place sorting)

### When to Use
- Small datasets (typically n < 20-30)
- Nearly sorted data (very efficient)
- Online sorting (when data arrives sequentially)
- As part of advanced algorithms (Timsort, hybrid sorts)

---

## Merge Sort
**📁 Implementation:** 
- [7. Merging two sorted arrays.py](./7.%20Merging%20two%20sorted%20arrays.py) - Base merge operation
- [8. Merge Subarrays.py](./8.%20Merge%20Subarrays.py) - Merging subarrays within single array
- [9. Merge Sort.py](./9.%20Merge%20Sort.py) - Complete recursive merge sort

### Logic
Merge Sort is a divide-and-conquer algorithm that divides the array into two halves, recursively sorts them, and then merges the sorted halves back together.

### How It Works
1. **Divide**: Split array into two halves until each subarray has one element
2. **Conquer**: Single elements are already sorted
3. **Merge**: Combine two sorted subarrays into one sorted array by comparing elements from each subarray

### Merge Process
- Use two pointers, one for each sorted subarray
- Compare elements at both pointers
- Add the smaller element to the result and advance that pointer
- Continue until all elements are merged

### Time Complexity

| Case | Complexity | Calculation |
|------|------------|-------------|
| **Best Case** | O(n log n) | Dividing: log₂(n) levels. Merging: n comparisons per level. Total: n × log₂(n) |
| **Average Case** | O(n log n) | Always divides array evenly and merges all elements at each level |
| **Worst Case** | O(n log n) | Same as best case - consistent performance regardless of input |

### Space Complexity
- **Auxiliary Space**: O(n) - Requires temporary arrays for merging. At any point, needs space proportional to n for the merge operation

### Key Characteristics
- **Stable**: Maintains relative order of equal elements
- **Predictable**: Always O(n log n), regardless of input
- **Not in-place**: Requires additional memory

### When to Use
- Large datasets
- When stability is required
- When predictable performance is needed
- External sorting (sorting data that doesn't fit in memory)
- Linked lists (works well with O(1) space on linked lists)

---

## Quick Sort
**📁 Implementation:**
- [13. Partition of a given array.py](./13.%20Partition%20of%20a%20given%20array.py) - Basic partition concept
- [14. Lomuto's Partition.py](./14.%20Lomuto's%20Partition.py) - Lomuto partition scheme
- [15. Hoarse's Partition.py](./15.%20Hoarse's%20Partition.py) - Hoarse partition scheme
- [16. QuickSort using Lomuto.py](./16.%20QuickSort%20using%20Lomuto.py) - Complete QuickSort with Lomuto
- [17. QuickSort using Hoarse.py](./17.%20QuickSort%20using%20Hoarse.py) - Complete QuickSort with Hoarse

### Logic
Quick Sort is a divide-and-conquer algorithm that selects a 'pivot' element and partitions the array so that elements smaller than the pivot are on the left and larger elements are on the right. It then recursively sorts the subarrays.

### Partition Schemes

#### Lomuto Partition
- **Pivot**: Last element of the array
- **Process**: Maintains an index for smaller elements, swaps elements as it scans
- **Simpler**: Easier to understand and implement
- **Performance**: Generally slower, more swaps

#### Hoarse Partition
- **Pivot**: Can be first, last, or middle element (often first)
- **Process**: Uses two pointers from both ends moving toward each other
- **Efficient**: Fewer swaps, better performance in practice
- **Original**: The original partitioning scheme by Tony Hoare

### How It Works (General)
1. Choose a pivot element
2. Partition the array around the pivot
3. Recursively apply the same process to left and right subarrays
4. Base case: subarray of size 1 or 0 is already sorted

### Time Complexity

| Case | Complexity | Calculation |
|------|------------|-------------|
| **Best Case** | O(n log n) | Pivot divides array evenly each time. Depth: log₂(n), Work per level: n. Total: n × log₂(n) |
| **Average Case** | O(n log n) | Pivot is reasonably balanced on average. Expected depth: log(n), Partitioning: n per level |
| **Worst Case** | O(n²) | Pivot is smallest/largest element every time (sorted/reverse sorted). Depth: n, Work: n + (n-1) + ... + 1 = n(n+1)/2 |

### Space Complexity
- **Auxiliary Space**: 
  - **Best/Average**: O(log n) - Recursion stack depth when partitions are balanced
  - **Worst**: O(n) - Recursion stack when partitions are completely unbalanced

### Key Characteristics
- **In-place**: Uses only a constant amount of extra space (excluding recursion stack)
- **Unstable**: Doesn't preserve relative order of equal elements
- **Cache-friendly**: Good locality of reference

### When to Use
- General-purpose sorting (most common choice)
- Large datasets
- When average-case performance matters more than worst-case
- When O(log n) space is acceptable

### Pivot Selection Strategies
- **First/Last element**: Simple but poor for sorted data
- **Random**: Avoids worst case with high probability
- **Median-of-three**: Takes median of first, middle, and last elements (good balance)

---

## Heap Sort
**📁 Implementation:** [18. Heap Sort.py](./18.%20Heap%20Sort.py)

### Logic
Heap Sort uses a binary heap data structure. It first builds a max heap from the array, then repeatedly extracts the maximum element (root) and places it at the end of the array, maintaining the heap property for the remaining elements.

### Binary Heap Basics
- **Complete Binary Tree**: All levels filled except possibly the last, which fills left to right
- **Max Heap Property**: Parent node ≥ child nodes
- **Array Representation**: For element at index i:
  - Left child: 2i + 1
  - Right child: 2i + 2
  - Parent: (i - 1) / 2

### How It Works
1. **Build Max Heap**: Convert array into a max heap
   - Start from last non-leaf node (n/2 - 1)
   - Heapify each subtree from bottom to top
2. **Extract Maximum**: 
   - Swap root (maximum) with last element
   - Reduce heap size by 1
   - Heapify the root to restore max heap property
3. Repeat step 2 until heap size is 1

### Heapify Operation
The process of maintaining heap property:
- Compare parent with children
- Swap with larger child if needed
- Recursively heapify the affected subtree

### Time Complexity

| Case | Complexity | Calculation |
|------|------------|-------------|
| **Best Case** | O(n log n) | Building heap: O(n). Extracting n elements: n × log(n). Total: O(n) + O(n log n) = O(n log n) |
| **Average Case** | O(n log n) | Same as best case - consistent performance |
| **Worst Case** | O(n log n) | Same as best case. Each heapify operation: O(log n), Performed n times |

### Space Complexity
- **Auxiliary Space**: O(1) - Sorts in place using the array itself as the heap (excluding recursion stack for heapify, which is O(log n))

### Key Characteristics
- **In-place**: Doesn't require extra array space
- **Unstable**: Doesn't preserve relative order of equal elements
- **Consistent**: Always O(n log n), regardless of input
- **Not adaptive**: Doesn't benefit from partially sorted data

### When to Use
- When consistent O(n log n) performance is required
- When space is limited (in-place sorting)
- When worst-case guarantees matter
- Priority queue implementations

---

## Comparison Summary

### Time Complexity Table

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

### Stability Comparison

| Algorithm | Stable? | Notes |
|-----------|---------|-------|
| Bubble Sort | Yes | Adjacent swaps preserve order |
| Selection Sort | No* | Can be made stable with modification |
| Insertion Sort | Yes | Elements shift, not swap |
| Merge Sort | Yes | Merge operation can preserve order |
| Quick Sort | No | Partitioning doesn't preserve order |
| Heap Sort | No | Heap operations destroy relative order |

### Quick Decision Guide

**Choose Bubble Sort when:**
- Dataset is very small (< 20 elements)
- Data is nearly sorted
- Simplicity is paramount

**Choose Selection Sort when:**
- Write operations are expensive
- Need minimal number of swaps

**Choose Insertion Sort when:**
- Dataset is small or nearly sorted
- Data arrives sequentially (online sorting)
- Used as part of hybrid algorithms

**Choose Merge Sort when:**
- Need guaranteed O(n log n)
- Stability is required
- Sorting linked lists
- External sorting

**Choose Quick Sort when:**
- General-purpose sorting
- Average performance matters most
- Memory for O(n) auxiliary space is unavailable

**Choose Heap Sort when:**
- Need guaranteed O(n log n) with O(1) space
- Implementing priority queues
- Worst-case time complexity matters

---

## Additional Sorting Concepts

### Counting Inversions
An inversion is a pair of indices (i, j) where i < j but arr[i] > arr[j]. The number of inversions indicates how far the array is from being sorted.

- **Significance**: Measures sortedness of an array
- **Applications**: Ranking similarity, collaborative filtering
- **Efficient Counting**: Modified merge sort can count inversions in O(n log n)

### Partitioning
Partitioning rearranges array elements around a pivot value:
- Elements ≤ pivot on the left
- Elements > pivot on the right
- Used in Quick Sort and Quick Select algorithms

### Array Operations

**Union of Sorted Arrays**: Merge two sorted arrays into one sorted array
- Similar to merge operation in merge sort
- Time: O(n + m), Space: O(n + m)

**Intersection of Sorted Arrays**: Find common elements
- Use two pointers, advance based on comparison
- Time: O(n + m), Space: O(min(n, m))

---

## Tips for Implementation

1. **Always test edge cases**: Empty array, single element, duplicates, already sorted
2. **Recursion depth**: Be aware of stack overflow for deep recursion (Quick Sort, Merge Sort)
3. **Index boundaries**: Off-by-one errors are common in sorting algorithms
4. **Stability matters**: Choose stable sorts when order of equal elements matters
5. **Hybrid approaches**: Real-world sorts often combine algorithms (e.g., Timsort uses Insertion Sort + Merge Sort)

---
