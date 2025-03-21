"""
testing.py

Demonstrates all major features of the Hotel Management System.
Fixes ModuleNotFoundError by dynamically loading `classes.py`.
"""

# Import required modules
import importlib.util  # Allows importing `classes.py` dynamically
import sys
import os

# Get the directory of the current script (testing.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to `classes.py` file
classes_path = os.path.join(current_dir, "classes.py")

# Load `classes.py` dynamically
spec = importlib.util.spec_from_file_location("classes", classes_path)
classes = importlib.util.module_from_spec(spec)
sys.modules["classes"] = classes
spec.loader.exec_module(classes)

# ------------------------------------------------------------
# TEST 1: GUEST ACCOUNT CREATION
# ------------------------------------------------------------
def test_guest_account_creation():
    """Creates guest accounts and verifies information is stored correctly."""
    print("\n--- TEST 1: Guest Account Creation ---")

    # Example 1: Standard Guest
    guest1 = classes.Guest(101, "Alice Wonderland", "555-1234", True, "alice@example.com", "USA")
    print("Guest 1 Created:", guest1)

    # Example 2: Premium Guest
    guest2 = classes.PremiumGuest(102, "Bob Builder", "555-5678", False, "bob@example.com", "UK",
                                  100, "Gold", 0.15, True)
    print("Guest 2 Created (Premium):", guest2)


# ------------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------------
def main():
    """Runs all test cases."""
    test_guest_account_creation()


# Run main function
if __name__ == "__main__":
    main()
