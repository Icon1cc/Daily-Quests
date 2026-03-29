"""
Implementing a Queue in Python using List.
"""

q = []
def enqueue(item):
    q.append(item)
    print(f"Enqueued: {item}")
def dequeue():
    if not is_empty():
        return q.pop(0)
    else:
        raise IndexError("Dequeue from an empty queue")
def display():
    return q
def get_front():
    if not is_empty():
        return q[0]
    else:
        return "Queue is empty"
def get_rear():
    if not is_empty():
        return q[-1]
    else:
        return "Queue is empty"
def is_empty():
    return len(q) == 0
def size():
    return len(q)   

# --- Demonstration ---
if __name__ == "__main__":  
    # 1. Enqueue operations
    enqueue("Apple")
    enqueue("Banana")
    enqueue("Cherry")

    # 2. Display Queue
    print("\nCurrent Queue:", display())

    # 3. Get Front and Rear
    print("Front element:", get_front())
    print("Rear element:", get_rear())

    # 4. Dequeue an element
    print("Dequeue element:", dequeue())

    # 5. Display Queue after Dequeue
    print("Queue after dequeue:", display())

    # 6. Check if the queue is empty
    print("Is the queue empty?", is_empty())

    # 7. Check the size of the queue
    print("Size of the queue:", size())

    