"""
Problem: Valid Parentheses
Difficulty: Easy

Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example:
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'
"""

def is_valid(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        s: String containing parentheses
        
    Returns:
        True if string is valid, False otherwise
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Pop from stack or use dummy value if stack is empty
            top_element = stack.pop() if stack else '#'
            
            if mapping[char] != top_element:
                return False
        else:
            # Push opening bracket onto stack
            stack.append(char)
    
    # Stack should be empty if all brackets are matched
    return not stack


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((", False),
        ("))", False),
        ("(())", True),
    ]
    
    print("Testing Valid Parentheses Solution:")
    print("-" * 50)
    
    for s, expected in test_cases:
        result = is_valid(s)
        
        print(f"Input: s = '{s}'")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"✓ Correct" if result == expected else "✗ Wrong")
        print("-" * 50)
