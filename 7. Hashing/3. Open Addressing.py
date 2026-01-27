"""
Implementation of Open Addressing using Linear Probing.
"""

# We use a unique object as a marker for deleted items. 
# This is distinct from 'None' (empty) and any user data.
TOMBSTONE = object()

class OpenAddressingHashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [None] * size
        self.count = 0  # Tracks active items

    def _hash(self, key):
        return abs(hash(key)) % self.size

    def insert(self, key, value):
        # 1. Check load factor and resize if needed
        if self.count / self.size >= 0.7:
            self._resize()

        index = self._hash(key)
        original_index = index
        first_tombstone_index = None

        # 2. Linear Probe to find key OR empty slot
        while self.table[index] is not None:
            # Check if this slot matches the key (Update existing)
            if self.table[index] is not TOMBSTONE and self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            # Record the first Tombstone we see (we can recycle this spot later!)
            if self.table[index] is TOMBSTONE and first_tombstone_index is None:
                first_tombstone_index = index

            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full (Should not happen with resize)")

        # 3. Insert the new item
        # If we found a tombstone along the way, use that spot (recycling).
        # Otherwise, use the empty (None) spot we just found.
        target_index = first_tombstone_index if first_tombstone_index is not None else index
        
        self.table[target_index] = (key, value)
        self.count += 1

    def search(self, key):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            # If it's not a tombstone and key matches, return value
            if self.table[index] is not TOMBSTONE and self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size
            if index == original_index:
                break
        
        return None

    def delete(self, key):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            # If found, mark as TOMBSTONE (Soft Delete)
            if self.table[index] is not TOMBSTONE and self.table[index][0] == key:
                self.table[index] = TOMBSTONE
                self.count -= 1
                return True

            index = (index + 1) % self.size
            if index == original_index:
                break
        
        return False

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            # Re-insert only valid items (skip None and TOMBSTONE)
            if item is not None and item is not TOMBSTONE:
                self.insert(item[0], item[1])

# --- Main Execution ---
if __name__ == "__main__":
    try:
        user_size = int(input("Enter the size of the Hash Table: "))
        ht = OpenAddressingHashTable(user_size)
        print(f"Successfully created a Hash Table of size {user_size}.\n")

        while True:
            # Clean inputs
            command_line = input("Enter command (insert <k> <v>, search <k>, delete <k>, exit): ").strip().split()
            if not command_line: continue
            
            cmd = command_line[0].lower()

            if cmd == "exit":
                break

            try:
                if cmd == "insert" and len(command_line) == 3:
                    ht.insert(command_line[1], command_line[2])
                    print(f"   -> Inserted {command_line[1]}")
                
                elif cmd == "search" and len(command_line) == 2:
                    res = ht.search(command_line[1])
                    print(f"   -> Found: {res}" if res else "   -> Not Found")

                elif cmd == "delete" and len(command_line) == 2:
                    deleted = ht.delete(command_line[1])
                    print(f"   -> Deleted." if deleted else "   -> Key not found.")
                
                else:
                    print("Invalid command format.")
            except Exception as e:
                print(f"Error: {e}")

    except ValueError:
        print("Invalid size input.")