"""
Problem: Binary Search
Difficulty: Easy

Description:
Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. If target exists, 
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique
- nums is sorted in ascending order
"""

def binary_search(nums, target):
    """
    Iterative binary search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        nums: Sorted array of integers
        target: Target value to search
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(nums, target):
    """
    Recursive binary search
    Time Complexity: O(log n)
    Space Complexity: O(log n) - recursion stack
    
    Args:
        nums: Sorted array of integers
        target: Target value to search
        
    Returns:
        Index of target if found, -1 otherwise
    """
    def search(left, right):
        if left > right:
            return -1
        
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)
    
    return search(0, len(nums) - 1)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 3, 2),
    ]
    
    print("Testing Binary Search Solutions:")
    print("-" * 50)
    
    for nums, target, expected in test_cases:
        result1 = binary_search(nums, target)
        result2 = binary_search_recursive(nums, target)
        
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Iterative: {result1}")
        print(f"Recursive: {result2}")
        print(f"✓ Correct" if result1 == expected else "✗ Wrong")
        print("-" * 50)
