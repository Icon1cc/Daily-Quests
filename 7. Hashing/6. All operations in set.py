"""
Write a python function to perform all operations (add, remove, discard, update and check existence) on a set data structure.
"""

class CustomSet:
    def __init__(self):
        self.data = set()

    def add(self, element):
        """Add an element to the set."""
        self.data.add(element)

    def remove(self, element):
        """
        Strict Removal: Raises KeyError if element not found.
        """
        self.data.remove(element)

    def discard(self, element):
        """
        Safe Removal: Does nothing if element not found.
        """
        self.data.discard(element)

    def exists(self, element):
        """Check if an element exists in the set."""
        return element in self.data

    def update(self, old_element, new_element):
        """
        Update an element in the set.
        (Removes old, Adds new).
        """
        if old_element in self.data:
            self.data.remove(old_element)
            self.data.add(new_element)
        else:
            raise KeyError(f"Element '{old_element}' not found in the set.")
    
    def __str__(self):
        return str(self.data)

# --- Main Execution ---
if __name__ == "__main__":
    try:
        # 1. Setup
        input_data = input("Enter initial elements (space-separated): ").strip()
        initial_elements = input_data.split() if input_data else []
        
        custom_set = CustomSet()
        for elem in initial_elements:
            custom_set.add(elem)    
        
        print(f"Initial set: {custom_set}")

        # 2. Test Add
        print("\n--- Adding 'test_item' ---")
        custom_set.add("test_item")
        print(f"Set: {custom_set}")

        # 3. Test Update
        print("\n--- Updating 'test_item' to 'updated_item' ---")
        custom_set.update("test_item", "updated_item")
        print(f"Set: {custom_set}")

        # 4. Test Remove (Strict)
        check_val = "updated_item"
        print(f"\n--- Removing '{check_val}' (Strict) ---")
        custom_set.remove(check_val)
        print(f"Set: {custom_set}")

        # 5. Test Discard (Safe) - The New Feature
        missing_val = "ghost_item"
        print(f"\n--- Discarding '{missing_val}' (Safe) ---")
        custom_set.discard(missing_val)
        print(f"Result: No Crash! Set is still: {custom_set}")
        
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")