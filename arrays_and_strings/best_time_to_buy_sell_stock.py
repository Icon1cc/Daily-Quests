"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy

Description:
You are given an array prices where prices[i] is the price of a given stock 
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you 
cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
profit = 6-1 = 5.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

def max_profit(prices):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        prices: List of stock prices
        
    Returns:
        Maximum profit possible
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit


def max_profit_brute_force(prices):
    """
    Brute force approach - checking all pairs
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    max_profit = 0
    n = len(prices)
    
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    
    return max_profit


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([2, 4, 1], 2),
    ]
    
    print("Testing Max Profit Solutions:")
    print("-" * 50)
    
    for prices, expected in test_cases:
        result1 = max_profit(prices)
        result2 = max_profit_brute_force(prices)
        
        print(f"Input: prices = {prices}")
        print(f"Expected: {expected}")
        print(f"Optimized Approach: {result1}")
        print(f"Brute Force Approach: {result2}")
        print(f"✓ Correct" if result1 == expected else "✗ Wrong")
        print("-" * 50)
