"""
Personal Finance Tracker
A command-line application to track income and expenses with CSV storage and visualization.
"""

import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import os

from data_entry import get_amount, get_date, get_category, get_description


class CSV:
    """Handles CSV file operations for financial transactions."""
    CSV_FILE = "finance_date.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        """Initialize CSV file if it doesn't exist."""
        if not os.path.exists(cls.CSV_FILE):
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
            print(f"✅ Created new finance file: {cls.CSV_FILE}")

    @classmethod
    def add_entry(cls, date, amount, category, description):
        """Add a new transaction entry to the CSV file."""
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("✅ Entry added successfully!")

    @classmethod
    def get_transaction_details(cls, start_date, end_date):
        """Retrieve and display transactions within a date range."""
        try:
            df = pd.read_csv(cls.CSV_FILE)
            if df.empty:
                print("❌ No transactions found in the database.")
                return pd.DataFrame()
            
            df["date"] = pd.to_datetime(df["date"], format=cls.FORMAT)
            start_date_obj = datetime.strptime(start_date, cls.FORMAT)
            end_date_obj = datetime.strptime(end_date, cls.FORMAT)
            
            mask = (df["date"] >= start_date_obj) & (df["date"] <= end_date_obj)
            filtered_df = df.loc[mask].copy()

            if filtered_df.empty:
                print("❌ No transactions found in the given date range.")
            else:
                print(f"\n{'='*70}")
                print(f"Transactions from {start_date} to {end_date}")
                print(f"{'='*70}")
                print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(cls.FORMAT)}))
                
                total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
                total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
                net_savings = total_income - total_expense
                
                print(f"\n{'='*70}")
                print(f"Total Income:   ${total_income:,.2f}")
                print(f"Total Expense:  ${total_expense:,.2f}")
                print(f"Net Savings:    ${net_savings:,.2f}")
                print(f"{'='*70}")

            return filtered_df
        except FileNotFoundError:
            print(f"❌ File {cls.CSV_FILE} not found. Please add a transaction first.")
            return pd.DataFrame()
        except Exception as e:
            print(f"❌ Error reading transactions: {e}")
            return pd.DataFrame()


def add_transaction():
    """Add a new financial transaction."""
    print("\n" + "="*50)
    print("Add New Transaction")
    print("="*50)
    date = get_date("Enter the date (DD-MM-YYYY) or press Enter for today's date: ", allow_default=True)
    amount = get_amount()
    description = get_description()
    category = get_category()
    CSV.add_entry(date, amount, category, description)


def plot_transactions(df):
    """Plot income and expenses over time."""
    if df.empty:
        print("❌ No data to plot.")
        return
    
    try:
        df_copy = df.copy()
        df_copy.set_index("date", inplace=True)
        
        # Resample by day and sum amounts
        income_df = df_copy[df_copy["category"] == "Income"].resample("D").sum()
        expense_df = df_copy[df_copy["category"] == "Expense"].resample("D").sum()
        
        plt.figure(figsize=(12, 6))
        plt.plot(income_df.index, income_df["amount"], label="Income", color="green", marker="o", linewidth=2)
        plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="red", marker="s", linewidth=2)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Amount ($)", fontsize=12)
        plt.title("Income and Expenses Over Time", fontsize=14, fontweight="bold")
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"❌ Error plotting transactions: {e}")


def main():
    """Main application loop."""
    CSV.initialize_csv()
    
    print("="*70)
    print("Personal Finance Tracker".center(70))
    print("="*70)
    
    is_running = True
    while is_running:
        print("\nOptions:")
        print("1. Add New Transaction")
        print("2. View Transactions (with date range)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            add_transaction()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            filtered_df = CSV.get_transaction_details(start_date, end_date)
            
            if not filtered_df.empty:
                plot_choice = input("\nDo you want to see plotted transactions? (y/n): ").lower().strip()
                if plot_choice == "y":
                    plot_transactions(filtered_df)
        elif choice == "3":
            print("\n👋 Thank you for using Personal Finance Tracker!")
            is_running = False
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting...")
