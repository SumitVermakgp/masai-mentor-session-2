"""
Calculator Exercise - Week 2 Python Workshop

This module contains basic mathematical functions.
Your job is to fix the bugs and complete the missing functions!

LEARNING FOCUS:
- Proper function naming (use descriptive names with snake_case)
- Clear documentation (docstrings)
- Code comments for complex logic
- Testing your code before committing

NAMING CONVENTION EXAMPLES:
✅ Good: calculate_average, add_numbers, get_total
❌ Bad: calc, add, x, func1
"""


def add_numbers(a, b):
    """
    Add two numbers together.

    This function works correctly - no changes needed!
    Use it as an example of a properly documented function.

    Args:
        a (int or float): The first number
        b (int or float): The second number

    Returns:
        int or float: The sum of a and b

    Example:
        >>> add_numbers(5, 3)
        8
    """
    return a + b


def subtract_numbers(a, b):
    """
    Subtract the second number from the first number.

    TODO: Fix this function - it's doing addition instead of subtraction!
    It should return a minus b

    Args:
        a (int or float): The first number
        b (int or float): The number to subtract

    Returns:
        int or float: The difference (a - b)

    Example:
        >>> subtract_numbers(10, 4)
        6
    """
    # BUG: This is doing addition, not subtraction!
    return a - b  # ← Fix this line!


def multiply_numbers(a, b):
    """
    Multiply two numbers together.

    TODO: Complete this function
    It should return a times b

    Args:
        a (int or float): The first number
        b (int or float): The second number

    Returns:
        int or float: The product of a and b

    Example:
        >>> multiply_numbers(6, 7)
        42
    """
    # DELETE the 'pass' statement below and write your code
    return a*b


def divide_numbers(a, b):
    """
    Divide the first number by the second number.

    TODO: Complete this function
    It should return a divided by b
    IMPORTANT: Handle the case when b is 0 (can't divide by zero!)

    Args:
        a (int or float): The number to divide (numerator)
        b (int or float): The number to divide by (denominator)

    Returns:
        float: The result of a / b, or None if b is 0

    Example:
        >>> divide_numbers(20, 4)
        5.0
        >>> divide_numbers(10, 0)
        None
    """
    # Hint: Use an if statement to check if b is 0 first!
    # If b is 0, return None
    # Otherwise, return a / b
    if b==0:
        return None

    return a/b # ← DELETE this line and write your code


def calculate_average(num1, num2, num3):
    """
    Calculate the average of three numbers.

    TODO: Fix this function
    The formula for average is: (num1 + num2 + num3) / 3

    Args:
        num1 (int or float): First number
        num2 (int or float): Second number
        num3 (int or float): Third number

    Returns:
        float: The average of the three numbers

    Example:
        >>> calculate_average(10, 20, 30)
        20.0
    """
    # BUG: We forgot to add num3 in the calculation!
    total = num1 + num2 +num3 # ← Fix this line!
    return total / 3


# =============================================================================
# TEST SECTION - DO NOT CHANGE THIS SECTION
# This code runs when you execute: python exercises/calculator.py
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CALCULATOR FUNCTIONS TEST")
    print("=" * 60)
    print("\nThis will show you if your functions work correctly!")
    print("Compare the 'Got' values with the 'Expected' values.\n")

    # Test 1: Addition (this should work!)
    print("Test 1: Addition")
    print(f"  Got:      5 + 3 = {add_numbers(5, 3)}")
    print(f"  Expected: 5 + 3 = 8")
    print(f"  Status: {'✓ PASS' if add_numbers(5, 3) == 8 else '✗ FAIL'}")
    print()

    # Test 2: Subtraction (this is broken!)
    print("Test 2: Subtraction")
    result = subtract_numbers(10, 4)
    print(f"  Got:      10 - 4 = {result}")
    print(f"  Expected: 10 - 4 = 6")
    print(f"  Status: {'✓ PASS' if result == 6 else '✗ FAIL'}")
    print()

    # Test 3: Multiplication (you need to complete this!)
    print("Test 3: Multiplication")
    try:
        result = multiply_numbers(6, 7)
        print(f"  Got:      6 * 7 = {result}")
        print(f"  Expected: 6 * 7 = 42")
        print(f"  Status: {'✓ PASS' if result == 42 else '✗ FAIL'}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 4: Division (you need to complete this!)
    print("Test 4: Division")
    try:
        result = divide_numbers(20, 4)
        print(f"  Got:      20 / 4 = {result}")
        print(f"  Expected: 20 / 4 = 5.0")
        print(f"  Status: {'✓ PASS' if result == 5.0 else '✗ FAIL'}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 5: Division by zero handling
    print("Test 5: Division by Zero")
    try:
        result = divide_numbers(10, 0)
        print(f"  Got:      10 / 0 = {result}")
        print(f"  Expected: 10 / 0 = None (can't divide by zero)")
        print(f"  Status: {'✓ PASS' if result is None else '✗ FAIL'}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 6: Average (this is broken!)
    print("Test 6: Average Calculation")
    result = calculate_average(10, 20, 30)
    print(f"  Got:      average of 10, 20, 30 = {result}")
    print(f"  Expected: average of 10, 20, 30 = 20.0")
    print(f"  Status: {'✓ PASS' if result == 20.0 else '✗ FAIL'}")
    print()

    print("=" * 60)
    print("\n💡 TIP: After fixing, save your work!")
    print("   git add exercises/calculator.py")
    print('   git commit -m "Fix calculator functions"')
    print("=" * 60)
