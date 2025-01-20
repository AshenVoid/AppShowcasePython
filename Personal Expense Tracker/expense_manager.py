class ExpenseManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_expense(self, date, amount, category, description):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.db_manager.add_expense(date, amount, category, description)

    def filter_expenses(self, category = None, date_range = None):
        expenses = self.db_manager.get_expenses()

        #TODO - Add pandas block to filter

        return expenses


    def calculate_summary(self):
        expenses = self.db_manager.get_expenses()

        #TODO: Add pandas block to summarize

        return expenses