"""
Problem: Contains Duplicate
Difficulty: Easy

Description:
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def contains_duplicate_set(nums):
    """
    Using set for O(1) lookup
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums: List of integers
        
    Returns:
        True if duplicate exists, False otherwise
    """
    return len(nums) != len(set(nums))


def contains_duplicate_dict(nums):
    """
    Using dictionary to track seen elements
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums: List of integers
        
    Returns:
        True if duplicate exists, False otherwise
    """
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False


def contains_duplicate_sort(nums):
    """
    Sort and check adjacent elements
    Time Complexity: O(n log n)
    Space Complexity: O(1) if sorting in-place
    
    Args:
        nums: List of integers
        
    Returns:
        True if duplicate exists, False otherwise
    """
    nums_sorted = sorted(nums)
    for i in range(len(nums_sorted) - 1):
        if nums_sorted[i] == nums_sorted[i + 1]:
            return True
    return False


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),
        ([1, 2], False),
    ]
    
    print("Testing Contains Duplicate Solutions:")
    print("-" * 50)
    
    for nums, expected in test_cases:
        result1 = contains_duplicate_set(nums)
        result2 = contains_duplicate_dict(nums)
        result3 = contains_duplicate_sort(nums)
        
        print(f"Input: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Set Approach: {result1}")
        print(f"Dict Approach: {result2}")
        print(f"Sort Approach: {result3}")
        print(f"✓ Correct" if result1 == expected else "✗ Wrong")
        print("-" * 50)
