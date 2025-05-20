# Expense Tracker
https://roadmap.sh/projects/expense-tracker

# Requirements
1. Users can add expense - description, amount
    $ expense-tracker add --description "Lunch" --amount 20
    Expense added successfully (ID: 1)
    $ expense-tracker add --description "Dinner" --amount 10
    Expense added successfully (ID: 2)

2. Users can del expense - input expense id?
    $ expense-tracker delete --id 2
    # Expense deleted successfully

3. Users can update expense - change description or amount

4. Users can view all expenses
    $ expense-tracker list
    # ID  Date       Description  Amount
    # 1   2024-08-06  Lunch        $20
    # 2   2024-08-06  Dinner       $10  

5. Users can view summary of all expenses
    $ expense-tracker summary
    # Total expenses: $30
    
6. Users can view summary of all expense in a specific month - input month
    $ expense-tracker summary --month 8
    # Total expenses for August: $20

# Additional
1. Expense category
2. Able to filter by category
3. Can set budget for each month and able to receive warning when overbudget
4. Export expense to CSV