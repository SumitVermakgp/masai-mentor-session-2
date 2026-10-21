"""
Student Information Exercise - Week 2 Python Workshop

This module contains functions for managing student information.
Fix the logic errors and complete the missing functions!

LEARNING FOCUS:
- Conditional statements (if-elif-else)
- Logical operators (and, or)
- Comparison operators (>=, <=, ==)
- Boolean return values (True/False)

NAMING CONVENTION REMINDER:
- Functions should start with verbs: calculate, get, check, is, has
- Variables should be nouns: student_score, grade_letter, total_marks
- Use descriptive names: is_passing (✅) vs pass_check (❌)
"""


def calculate_grade(score):
    """
    Convert a numerical score to a letter grade.

    TODO: Fix the logic errors in this function
    The grade assignments are all mixed up!

    Grade rules:
    - 90 to 100: 'A'
    - 80 to 89:  'B'
    - 70 to 79:  'C'
    - 60 to 69:  'D'
    - Below 60:  'F'

    Args:
        score (int or float): The student's score (0-100)

    Returns:
        str: The letter grade ('A', 'B', 'C', 'D', or 'F')

    Example:
        >>> calculate_grade(95)
        'A'
        >>> calculate_grade(75)
        'C'
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'  # ← BUG: Should be 'C'!
    elif score >= 60:
        return 'D'  # ← BUG: Should be 'D'!
    else:
        return 'F'


def is_passing(score):
    """
    Check if a student's score is passing.

    TODO: Complete this function
    A passing score is 60 or above.

    Args:
        score (int or float): The student's score

    Returns:
        bool: True if score >= 60, False otherwise

    Example:
        >>> is_passing(70)
        True
        >>> is_passing(50)
        False
    """
    # TODO: Your code here
    # Hint: Use a comparison operator and return True or False
    # You can do this in one line: return score >= 60
    if score >= 60:
        return True
    else:
        return False


def get_student_status(age, grade):
    """
    Determine a student's academic status based on age and grade level.

    TODO: Fix this function - ALL the return values are wrong!

    Rules:
    - If age < 18 AND grade >= 9:  return "High School"
    - If age >= 18 AND grade >= 12: return "College Ready"
    - Otherwise:                     return "Keep Studying"

    Args:
        age (int): The student's age
        grade (int): The student's grade level (1-12)

    Returns:
        str: The student's status

    Example:
        >>> get_student_status(16, 10)
        "High School"
        >>> get_student_status(18, 12)
        "College Ready"
    """
    # Check if student is under 18 and in grade 9 or above
    if age < 18 and grade >= 9:
        return "High School"  # ← BUG: Should be "High School"!

    # Check if student is 18+ and has completed grade 12
    elif age >= 18 and grade >= 12:
        return "College Ready"  # ← BUG: Should be "College Ready"!

    # All other cases
    else:
        return "Keep Studying"  # ← BUG: Should be "Keep Studying"!


def calculate_attendance_status(classes_attended, total_classes):
    """
    Calculate attendance percentage and return status.

    TODO: Complete this function

    Calculate the attendance percentage and return:
    - "Excellent"         if >= 90%
    - "Good"              if >= 75% and < 90%
    - "Needs Improvement" if >= 60% and < 75%
    - "Poor"              if < 60%

    Args:
        classes_attended (int): Number of classes the student attended
        total_classes (int): Total number of classes

    Returns:
        str: The attendance status

    Example:
        >>> calculate_attendance_status(18, 20)  # 90%
        "Excellent"
        >>> calculate_attendance_status(15, 20)  # 75%
        "Good"
    """
    # TODO: Your code here
    # Step 1: Calculate percentage = (classes_attended / total_classes) * 100
    # Step 2: Use if-elif-else to return the appropriate status

    percentage = (classes_attended / total_classes) * 100
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Good"
    elif percentage >= 60:
        return "Needs Improvement"
    else:
        return "Poor"


def check_eligibility(score, attendance_percent):
    """
    Check if a student is eligible for honors based on score and attendance.

    TODO: Complete this function

    A student is eligible for honors if:
    - Score is 85 or above AND
    - Attendance is 90% or above

    Args:
        score (int or float): The student's score
        attendance_percent (int or float): Attendance percentage

    Returns:
        bool: True if eligible for honors, False otherwise

    Example:
        >>> check_eligibility(90, 95)
        True
        >>> check_eligibility(90, 85)
        False
        >>> check_eligibility(80, 95)
        False
    """
    # TODO: Your code here
    # Hint: Use 'and' operator to check both conditions
    if score >= 85 and attendance_percent >= 90:
        return True
    else:
        return False


# =============================================================================
# TEST SECTION - DO NOT CHANGE THIS SECTION
# This code runs when you execute: python exercises/student_info.py
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("STUDENT INFO FUNCTIONS TEST")
    print("=" * 60)
    print("\nThis will show you if your functions work correctly!")
    print("Compare the 'Got' values with the 'Expected' values.\n")

    # Test 1: Grade calculation
    print("Test 1: Grade Calculation")
    test_scores = [(95, 'A'), (85, 'B'), (75, 'C'), (65, 'D'), (55, 'F')]
    all_passed = True
    for score, expected in test_scores:
        result = calculate_grade(score)
        status = '✓' if result == expected else '✗'
        if result != expected:
            all_passed = False
        print(f"  Score {score:3d}: Got '{result}', Expected '{expected}' {status}")
    print(f"  Overall: {'✓ PASS' if all_passed else '✗ FAIL'}")
    print()

    # Test 2: Passing check
    print("Test 2: Passing Check")
    try:
        result1 = is_passing(70)
        result2 = is_passing(50)
        print(f"  Score 70 is passing: Got {result1}, Expected True")
        print(f"  Score 50 is passing: Got {result2}, Expected False")
        status = '✓ PASS' if (result1 == True and result2 == False) else '✗ FAIL'
        print(f"  Status: {status}")
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
    print()

    # Test 3: Student status
    print("Test 3: Student Status")
    status_tests = [
        (16, 10, "High School"),
        (18, 12, "College Ready"),
        (15, 8, "Keep Studying")
    ]
    all_passed = True
    for age, grade, expected in status_tests:
        try:
            result = get_student_status(age, grade)
            status = '✓' if result == expected else '✗'
            if result != expected:
                all_passed = False
            print(f"  Age {age}, Grade {grade:2d}: Got '{result}', Expected '{expected}' {status}")
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            all_passed = False
    print(f"  Overall: {'✓ PASS' if all_passed else '✗ FAIL'}")
    print()

    # Test 4: Attendance status
    print("Test 4: Attendance Status")
    attendance_tests = [
        (18, 20, "Excellent"),  # 90%
        (16, 20, "Good"),       # 80%
        (13, 20, "Needs Improvement"),  # 65%
        (10, 20, "Poor")        # 50%
    ]
    all_passed = True
    for attended, total, expected in attendance_tests:
        try:
            result = calculate_attendance_status(attended, total)
            percentage = (attended / total) * 100
            status = '✓' if result == expected else '✗'
            if result != expected:
                all_passed = False
            print(f"  {attended}/{total} ({percentage:.0f}%): Got '{result}', Expected '{expected}' {status}")
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            all_passed = False
    print(f"  Overall: {'✓ PASS' if all_passed else '✗ FAIL'}")
    print()

    # Test 5: Eligibility check
    print("Test 5: Honors Eligibility")
    eligibility_tests = [
        (90, 95, True),   # High score, high attendance
        (90, 85, False),  # High score, low attendance
        (80, 95, False),  # Low score, high attendance
        (85, 90, True)    # Both at threshold
    ]
    all_passed = True
    for score, attendance, expected in eligibility_tests:
        try:
            result = check_eligibility(score, attendance)
            status = '✓' if result == expected else '✗'
            if result != expected:
                all_passed = False
            print(f"  Score {score}, Attendance {attendance}%: Got {result}, Expected {expected} {status}")
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            all_passed = False
    print(f"  Overall: {'✓ PASS' if all_passed else '✗ FAIL'}")
    print()

    print("=" * 60)
    print("\n💡 TIP: After fixing, save your work!")
    print("   git add exercises/student_info.py")
    print('   git commit -m "Fix logic errors in student functions"')
    print("=" * 60)
