"""
String Comparison Operators: <, <=, >, >=, !=, ==
"""

def demo_operators():
    s1 = "apple"
    s2 = "banana"
    s3 = "apple"
    
    # 1. Less Than (<)
    # True if s1 comes BEFORE s2 in the dictionary
    print(f"'{s1}' < '{s2}':  {s1 < s2}")   # True ('a' < 'b')

    # 2. Less Than or Equal (<=)
    # True if s1 is before s2 OR they are identical
    print(f"'{s1}' <= '{s3}': {s1 <= s3}")  # True (they are equal)

    # 3. Greater Than (>)
    # True if s2 comes AFTER s1
    print(f"'{s2}' > '{s1}':  {s2 > s1}")   # True ('b' > 'a')

    # 4. Greater Than or Equal (>=)
    print(f"'{s1}' >= '{s3}': {s1 >= s3}")  # True

    # 5. Equal To (==)
    # True only if contents are exactly the same
    print(f"'{s1}' == '{s3}': {s1 == s3}")  # True
    print(f"'{s1}' == '{s2}': {s1 == s2}")  # False

    # 6. Not Equal (!=)
    print(f"'{s1}' != '{s2}': {s1 != s2}")  # True

    # --- Special Case: ASCII Values ---
    # Uppercase 'Z' comes BEFORE lowercase 'a' in ASCII table
    print("\n--- ASCII Case Check ---")
    print(f"'Z' < 'a': {'Z' < 'a'}")        # True (90 < 97)

if __name__ == "__main__":
    demo_operators()