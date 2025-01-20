from database_manager import DatabaseManager
from expense_manager import ExpenseManager
from visualizer import ExpenseVisualizer

class ExpenseTrackerApp:
    def __init__(self):
        self.db_manager = DatabaseManager("expenses.db")
        self.expense_manager = ExpenseManager(self.db_manager)
        self.visualizer = ExpenseVisualizer()

    def run(self):
        #TODO - UI & tie together
        pass


if __name__ == "__main__":
    app = ExpenseTrackerApp()
    app.run()