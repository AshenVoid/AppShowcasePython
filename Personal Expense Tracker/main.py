import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from database_manager import DatabaseManager
from expense_manager import ExpenseManager
from visualizer import ExpenseVisualizer

class ExpenseTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(100,100,600,400)

        self.db_manager = DatabaseManager("expenses.db")
        self.expense_manager = ExpenseManager(self.db_manager)
        self.visualizer = ExpenseVisualizer()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        #TITLE
        self.title_label = QLabel("Welcome to Expense Tracker!")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        #ADD_EXPENSE
        self.add_expense_button = QPushButton("Add Expense")
        self.add_expense_button.clicked.connect(self.add_expense_action)
        layout.addWidget(self.add_expense_button)



if __name__ == "__main__":
    app = ExpenseTrackerApp()
