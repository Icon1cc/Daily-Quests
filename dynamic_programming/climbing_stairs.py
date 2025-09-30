"""
Problem: Climbing Stairs
Difficulty: Easy

Description:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45
"""

def climb_stairs_dp(n):
    """
    Dynamic Programming approach (bottom-up)
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Number of steps
        
    Returns:
        Number of distinct ways to climb to the top
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def climb_stairs_optimized(n):
    """
    Optimized space complexity using only two variables
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Number of steps
        
    Returns:
        Number of distinct ways to climb to the top
    """
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


def climb_stairs_recursive(n):
    """
    Recursive approach with memoization (top-down)
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Number of steps
        
    Returns:
        Number of distinct ways to climb to the top
    """
    memo = {}
    
    def climb(n):
        if n <= 2:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] = climb(n - 1) + climb(n - 2)
        return memo[n]
    
    return climb(n)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
    ]
    
    print("Testing Climbing Stairs Solutions:")
    print("-" * 50)
    
    for n, expected in test_cases:
        result1 = climb_stairs_dp(n)
        result2 = climb_stairs_optimized(n)
        result3 = climb_stairs_recursive(n)
        
        print(f"Input: n = {n}")
        print(f"Expected: {expected}")
        print(f"DP Approach: {result1}")
        print(f"Optimized Approach: {result2}")
        print(f"Recursive + Memo: {result3}")
        print(f"✓ Correct" if result1 == expected else "✗ Wrong")
        print("-" * 50)
