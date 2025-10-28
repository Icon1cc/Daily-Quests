"""
Problem: Reverse Linked List
Difficulty: Easy

Description:
Given the head of a singly linked list, reverse the list, and return the 
reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Constraints:
- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000
"""

class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    Iterative approach to reverse linked list
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev


def reverse_list_recursive(head):
    """
    Recursive approach to reverse linked list
    Time Complexity: O(n)
    Space Complexity: O(n) - recursion stack
    
    Args:
        head: Head of the linked list
        
    Returns:
        Head of the reversed linked list
    """
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head


def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to Python list."""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        [],
    ]
    
    print("Testing Reverse Linked List Solutions:")
    print("-" * 50)
    
    for values in test_cases:
        # Test iterative approach
        head1 = create_linked_list(values)
        reversed_head1 = reverse_list(head1)
        result1 = linked_list_to_list(reversed_head1)
        
        # Test recursive approach
        head2 = create_linked_list(values)
        reversed_head2 = reverse_list_recursive(head2)
        result2 = linked_list_to_list(reversed_head2)
        
        expected = values[::-1]
        
        print(f"Input: {values}")
        print(f"Expected: {expected}")
        print(f"Iterative Approach: {result1}")
        print(f"Recursive Approach: {result2}")
        print(f"✓ Correct" if result1 == expected else "✗ Wrong")
        print("-" * 50)
