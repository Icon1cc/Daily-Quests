"""
Write a function to delete the head of a doubly linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delete_head(head):
    # If the list is empty, return None
    if head is None:
        return None
    
    # If the list has only one node, return None after deletion
    if head.next is None:
        return None
    
    # Move head to the next node
    new_head = head.next
    new_head.prev = None  # Set the new head's prev to None
    return new_head       # Return the new head

# Helper function to create list from user input
def create_doubly_linked_list(arr):
    if not arr:
        return None
    
    head = Node(int(arr[0]))
    current = head
    
    for i in range(1, len(arr)):
        new_node = Node(int(arr[i]))
        current.next = new_node  # Link forward
        new_node.prev = current  # Link backward
        current = new_node       # Move current
        
    return head

def display(head):
    if not head:
        print("List is empty")
        return
    nodes = []
    temp = head
    while temp:
        nodes.append(str(temp.data))
        temp = temp.next
    print(" <-> ".join(nodes))
# --- Main Execution ---    
# 1. Get input for the initial list
user_input = input("Enter the list values separated by space (e.g., 10 20 30): ")
values = user_input.split() 
# Create the list
head = create_doubly_linked_list(values)
print("Original List:")
display(head)   