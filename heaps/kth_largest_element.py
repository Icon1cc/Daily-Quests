"""
Problem: Kth Largest Element in an Array
Difficulty: Medium

Description:
Given an integer array nums and an integer k, return the kth largest 
element in the array.

Note that it is the kth largest element in the sorted order, not the 
kth distinct element.

Can you solve it without sorting?

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

import heapq


def find_kth_largest_heap(nums, k):
    """
    Using min heap of size k
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    
    Args:
        nums: List of integers
        k: kth largest to find
        
    Returns:
        kth largest element
    """
    # Maintain a min heap of size k
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]


def find_kth_largest_sort(nums, k):
    """
    Sorting approach
    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sort implementation
    
    Args:
        nums: List of integers
        k: kth largest to find
        
    Returns:
        kth largest element
    """
    nums.sort(reverse=True)
    return nums[k - 1]


def find_kth_largest_quickselect(nums, k):
    """
    QuickSelect algorithm (average O(n))
    Time Complexity: O(n) average, O(n^2) worst case
    Space Complexity: O(1)
    
    Args:
        nums: List of integers
        k: kth largest to find
        
    Returns:
        kth largest element
    """
    k = len(nums) - k  # Convert to kth smallest for easier implementation
    
    def quickselect(left, right):
        pivot = nums[right]
        p = left
        
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        nums[p], nums[right] = nums[right], nums[p]
        
        if p > k:
            return quickselect(left, p - 1)
        elif p < k:
            return quickselect(p + 1, right)
        else:
            return nums[p]
    
    return quickselect(0, len(nums) - 1)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 6, 5, 4, 3, 2, 1], 2, 6),
    ]
    
    print("Testing Kth Largest Element Solutions:")
    print("-" * 50)
    
    for nums, k, expected in test_cases:
        # Make copies since quickselect modifies the array
        nums1 = nums.copy()
        nums2 = nums.copy()
        nums3 = nums.copy()
        
        result1 = find_kth_largest_heap(nums1, k)
        result2 = find_kth_largest_sort(nums2, k)
        result3 = find_kth_largest_quickselect(nums3, k)
        
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Heap Approach: {result1}")
        print(f"Sort Approach: {result2}")
        print(f"QuickSelect: {result3}")
        print(f"✓ Correct" if result1 == expected else "✗ Wrong")
        print("-" * 50)
