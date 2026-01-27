"""
Write a python function to perform all operations (add, remove, update and check existence) on a set data structure.
"""

class CustomSet:
    def __init__(self):
        self.data = set()

    def add(self, element):
        """Add an element to the set."""
        self.data.add(element)

    def remove(self, element):
        """
        Remove an element from the set. 
        Raises KeyError if not found (standard Python set behavior).
        """
        self.data.remove(element)

    def exists(self, element):
        """Check if an element exists in the set."""
        return element in self.data

    def update(self, old_element, new_element):
        """
        Update an element in the set.
        Since sets are unordered, 'updating' really means 
        removing the old one and adding the new one.
        """
        if old_element in self.data:
            self.data.remove(old_element)
            self.data.add(new_element)
        else:
            raise KeyError(f"Element '{old_element}' not found in the set.")
    
    # Optional: Helper to make printing the object prettier
    def __str__(self):
        return str(self.data)

# --- Main Execution ---
if __name__ == "__main__":
    try:
        # 1. Clean input handling
        input_data = input("Enter initial elements (space-separated): ").strip()
        
        # Handle empty input gracefully
        initial_elements = input_data.split() if input_data else []
        
        custom_set = CustomSet()
        
        # 2. Populate Set
        for elem in initial_elements:
            custom_set.add(elem)    
        
        print(f"Initial set: {custom_set}")

        # 3. Test Add
        print("\n--- Adding 'test_item' ---")
        custom_set.add("test_item")
        print(f"Set: {custom_set}")

        # 4. Test Update
        print("\n--- Updating 'test_item' to 'updated_item' ---")
        custom_set.update("test_item", "updated_item")
        print(f"Set: {custom_set}")

        # 5. Test Exists
        check_val = "updated_item"
        is_there = custom_set.exists(check_val)
        print(f"\n--- Does '{check_val}' exist? {is_there} ---")

        # 6. Test Remove
        print(f"\n--- Removing '{check_val}' ---")
        custom_set.remove(check_val)
        print(f"Set: {custom_set}")
        
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")