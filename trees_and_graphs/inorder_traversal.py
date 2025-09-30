"""
Problem: Binary Tree Inorder Traversal
Difficulty: Easy

Description:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal: Left -> Root -> Right

Example:
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1,3,2]

Constraints:
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal_recursive(root):
    """
    Recursive approach to inorder traversal
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List of node values in inorder
    """
    result = []
    
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result


def inorder_traversal_iterative(root):
    """
    Iterative approach using stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List of node values in inorder
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Current is None, pop from stack
        current = stack.pop()
        result.append(current.val)
        
        # Visit right subtree
        current = current.right
    
    return result


if __name__ == "__main__":
    # Test case 1: [1,null,2,3]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    
    # Test case 2: [1,2,3,4,5]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    
    # Test case 3: Empty tree
    root3 = None
    
    # Test case 4: Single node
    root4 = TreeNode(1)
    
    test_cases = [
        (root1, [1, 3, 2]),
        (root2, [4, 2, 5, 1, 3]),
        (root3, []),
        (root4, [1]),
    ]
    
    print("Testing Binary Tree Inorder Traversal:")
    print("-" * 50)
    
    for i, (root, expected) in enumerate(test_cases, 1):
        result_recursive = inorder_traversal_recursive(root)
        result_iterative = inorder_traversal_iterative(root)
        
        print(f"Test Case {i}:")
        print(f"Expected: {expected}")
        print(f"Recursive: {result_recursive}")
        print(f"Iterative: {result_iterative}")
        print(f"✓ Correct" if result_recursive == expected else "✗ Wrong")
        print("-" * 50)
