# 💰 Personal Finance Tracker

A comprehensive command-line application to track income and expenses with CSV storage and data visualization. Perfect for personal budgeting and financial management.

## Features

- 💵 Add income and expense transactions
- 📅 Date-based transaction filtering
- 📊 Financial summaries (total income, expenses, net savings)
- 📈 Data visualization with matplotlib
- 💾 CSV data persistence
- ✅ Input validation and error handling
- 🎨 User-friendly interface

## Requirements

- Python 3.6 or higher
- `pandas` - Data manipulation
- `matplotlib` - Data visualization

## Installation

### Install Dependencies

**Option 1: Using requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option 2: Manual installation**
```bash
pip install pandas matplotlib
```

## Usage

```bash
python main.py
```

### Main Menu

```
======================================================================
                    Personal Finance Tracker
======================================================================

Options:
1. Add New Transaction
2. View Transactions (with date range)
3. Exit

Enter your choice (1-3):
```

## Features in Detail

### 1. Add New Transaction

- **Date**: Enter date in DD-MM-YYYY format (or press Enter for today)
- **Amount**: Enter positive amount
- **Category**: Choose 'I' for Income or 'E' for Expense
- **Description**: Optional description

### 2. View Transactions

- Enter start and end dates
- View all transactions in the date range
- See summary:
  - Total Income
  - Total Expenses
  - Net Savings
- Optional: View plotted transactions

### 3. Data Visualization

The application can generate line charts showing:
- Income over time (green line)
- Expenses over time (red line)
- Visual comparison of financial trends

## Project Structure

```
PERSONAL FINANCE TRACKER/
├── main.py              # Main application logic
├── data_entry.py        # Input validation functions
├── finance_date.csv     # Data storage (auto-generated)
└── README.md           # This file
```

## Data Storage

Transactions are stored in `finance_date.csv` with the following structure:

| date | amount | category | description |
|------|--------|----------|------------|
| 15-11-2025 | 5000.00 | Income | Salary |
| 16-11-2025 | 50.00 | Expense | Groceries |

## Code Structure

### main.py
- `CSV` class: Handles CSV file operations
  - `initialize_csv()`: Creates CSV if it doesn't exist
  - `add_entry()`: Adds new transaction
  - `get_transaction_details()`: Retrieves and filters transactions
- `add_transaction()`: User interface for adding transactions
- `plot_transactions()`: Generates visualization
- `main()`: Main application loop

### data_entry.py
- `get_date()`: Validates and gets date input
- `get_amount()`: Validates and gets amount input
- `get_category()`: Validates and gets category input
- `get_description()`: Gets optional description

## Example Workflow

1. **Add Income**:
   ```
   Enter the date (DD-MM-YYYY) or press Enter for today's date: 
   Enter the amount: 5000
   Enter the category ('I' for income, 'E' for expense): I
   Enter a description (optional): Monthly Salary
   ✅ Entry added successfully!
   ```

2. **Add Expense**:
   ```
   Enter the date (DD-MM-YYYY) or press Enter for today's date: 16-11-2025
   Enter the amount: 150.50
   Enter the category ('I' for income, 'E' for expense): E
   Enter a description (optional): Grocery Shopping
   ✅ Entry added successfully!
   ```

3. **View Summary**:
   ```
   Enter the start date (dd-mm-yyyy): 01-11-2025
   Enter the end date (dd-mm-yyyy): 30-11-2025
   
   ======================================================================
   Transactions from 01-11-2025 to 30-11-2025
   ======================================================================
   ...
   
   ======================================================================
   Total Income:   $5,000.00
   Total Expense:  $1,250.50
   Net Savings:    $3,749.50
   ======================================================================
   ```

## Customization

### Date Format
Modify `DATE_FORMAT` in `data_entry.py`:
```python
DATE_FORMAT = "%d-%m-%Y"  # Change to "%Y-%m-%d" for ISO format
```

### CSV File Location
Modify `CSV_FILE` in `main.py`:
```python
CSV_FILE = "finance_date.csv"  # Change path as needed
```

### Chart Appearance
Modify `plot_transactions()` in `main.py` to customize:
- Colors
- Chart size
- Markers
- Grid style

## Error Handling

The application handles:
- Invalid date formats
- Negative or zero amounts
- Invalid categories
- Missing CSV file
- Empty date ranges
- File permission errors

## Tips for Use

1. **Regular Updates**: Add transactions daily for accurate tracking
2. **Descriptive Notes**: Use descriptions to remember what expenses were for
3. **Review Regularly**: Check your summary weekly/monthly
4. **Backup Data**: Keep a backup of `finance_date.csv`
5. **Date Ranges**: Use date ranges to analyze specific periods

## Future Enhancements

Potential features to add:
- Budget limits and alerts
- Category-based analysis
- Export to Excel/PDF
- Recurring transactions
- Multiple currency support
- Data backup/restore

## License

This project is open source and available for educational purposes.

---

**Take control of your finances! 💰**

