"""
Problem: Two Sum
Difficulty: Easy

Description:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists
"""

def two_sum(nums, target):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_brute_force(nums, target):
    """
    Brute force approach - checking all pairs
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
    ]
    
    print("Testing Two Sum Solutions:")
    print("-" * 50)
    
    for nums, target, expected in test_cases:
        result1 = two_sum(nums, target)
        result2 = two_sum_brute_force(nums, target)
        
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Hash Map Approach: {result1}")
        print(f"Brute Force Approach: {result2}")
        print(f"✓ Correct" if result1 == expected else "✗ Wrong")
        print("-" * 50)
