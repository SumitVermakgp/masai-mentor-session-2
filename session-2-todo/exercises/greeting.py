"""
Greeting Exercise - Week 2 Python Workshop

This module contains string manipulation functions.
Complete the missing functions and fix the bugs!

LEARNING FOCUS:
- String concatenation using the + operator
- Converting numbers to strings using str()
- Proper spacing in string formatting
- Writing clear docstrings

CODE COMMENT BEST PRACTICES:
✅ Good: "# Convert age to string for concatenation"
❌ Bad: "# This is a variable"
✅ Good: "# Calculate percentage to determine status"
❌ Bad: "# Add numbers"

Remember: Comment WHY you're doing something, not WHAT you're doing!
"""


def create_greeting(name):
    """
    Create a greeting message for a person.

    Args:
        name (str): The person's name

    Returns:
        str: A greeting message

    """
    return "Hello, " + name + "!"


def create_goodbye(name):
    """
    Create a goodbye message for a person.

    Args:
        name (str): The person's name

    Returns:
        str: A goodbye message

    """
    return f"Goodbye, {name}!"


def create_introduction(name, age):
    """
    Create an introduction message with name and age.

    Args:
        name (str): The person's name
        age (int): The person's age

    Returns:
        str: An introduction message

    """
    return "My name is " + name + " and I am " + str(age) + " years old."


def create_welcome_message(name, city):
    """
    Create a welcome message with name and city.

    Args:
        name (str): The person's name
        city (str): The person's city

    Returns:
        str: A welcome message

    """

    message = "Welcome " + name + " from " + city + "!"
    return message


def create_full_greeting(name, age, city):
    """
    Create a detailed greeting with name, age, and city.

    Args:
        name (str): The person's name
        age (int): The person's age
        city (str): The person's city

    Returns:
        str: A detailed greeting message

    Example:
        >>> create_full_greeting("Bob", 25, "Delhi")
        "Hello Bob! You are 25 years old and from Delhi."
    """
    return "Hello " + name + "! You are " + str(age) + " years old and from " + city + "."


# =============================================================================
# TEST SECTION - DO NOT CHANGE THIS SECTION
# This code runs when you execute: python exercises/greeting.py
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GREETING FUNCTIONS TEST")
    print("=" * 60)
    print("\nThis will show you if your functions work correctly!")
    print("Compare the 'Got' values with the 'Expected' values.\n")

    # Test 1: create_greeting
    print("Test 1: Basic Greeting")
    try:
        result = create_greeting("Student")
        print(f"  Got:      '{result}'")
        print(f"  Expected: 'Hello, Student!'")
        print(f"  Status: {'✓ PASS' if result == 'Hello, Student!' else '✗ FAIL'}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 2: create_goodbye
    print("Test 2: Goodbye Message")
    try:
        result = create_goodbye("Teacher")
        print(f"  Got:      '{result}'")
        print(f"  Expected: 'Goodbye, Teacher!'")
        print(f"  Status: {'✓ PASS' if result == 'Goodbye, Teacher!' else '✗ FAIL'}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 3: create_introduction
    print("Test 3: Introduction with Age")
    try:
        result = create_introduction("Alice", 20)
        print(f"  Got:      '{result}'")
        print(f"  Expected: 'My name is Alice and I am 20 years old.'")
        expected = "My name is Alice and I am 20 years old."
        print(f"  Status: {'✓ PASS' if result == expected else '✗ FAIL'}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 4: create_welcome_message
    print("Test 4: Welcome Message")
    try:
        result = create_welcome_message("Bob", "Delhi")
        print(f"  Got:      '{result}'")
        print(f"  Expected: 'Welcome Bob from Delhi!'")
        print(f"  Status: {'✓ PASS' if result == 'Welcome Bob from Delhi!' else '✗ FAIL'}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 5: create_full_greeting
    print("Test 5: Full Greeting")
    try:
        result = create_full_greeting("Charlie", 22, "Mumbai")
        print(f"  Got:      '{result}'")
        print(f"  Expected: 'Hello Charlie! You are 22 years old and from Mumbai.'")
        expected = "Hello Charlie! You are 22 years old and from Mumbai."
        print(f"  Status: {'✓ PASS' if result == expected else '✗ FAIL'}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    print("=" * 60)
    print("\n💡 TIP: After fixing, save your work!")
    print("   git add exercises/greeting.py")
    print('   git commit -m "Complete greeting functions"')
    print("=" * 60)