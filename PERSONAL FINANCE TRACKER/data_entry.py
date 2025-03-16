from datetime import datetime

from unicodedata import category

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")

    # this is a recursion as if it is not tried properly except again calls the get_date ()function with its parameters
    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%Y")
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format , Please enter the date in dd-mm-yyyy format  ")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount :"))
        if amount <= 0:
            raise ValueError("Amount cannot be negative , Plz Enter a proper amount...")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter the category ('I'for income and 'E' for expense : ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid cateogry , Please Enter 'I' for income or 'E' for expense ")


def get_description():
    return input("Enter a description (optional) :")
