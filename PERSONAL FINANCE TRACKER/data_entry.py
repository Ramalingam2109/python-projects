"""
Data Entry Module for Personal Finance Tracker
Handles user input validation for financial transactions.
"""

from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(prompt, allow_default=False):
    """
    Get and validate date input from user.
    
    Args:
        prompt: Input prompt string
        allow_default: If True, allows empty input to default to today's date
    
    Returns:
        str: Formatted date string (dd-mm-yyyy)
    """
    date_str = input(prompt).strip()
    
    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)

    try:
        valid_date = datetime.strptime(date_str, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("❌ Invalid date format. Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)


def get_amount():
    """
    Get and validate amount input from user.
    
    Returns:
        float: Positive amount value
    """
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("❌ Amount must be positive. Please enter a valid amount.")
        return round(amount, 2)
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    """
    Get and validate category input from user.
    
    Returns:
        str: Category name ("Income" or "Expense")
    """
    while True:
        category_input = input("Enter the category ('I' for income, 'E' for expense): ").upper().strip()
        if category_input in CATEGORIES:
            return CATEGORIES[category_input]
        print("❌ Invalid category. Please enter 'I' for income or 'E' for expense.")


def get_description():
    """
    Get optional description from user.
    
    Returns:
        str: Description string
    """
    description = input("Enter a description (optional): ").strip()
    return description if description else "No description"
