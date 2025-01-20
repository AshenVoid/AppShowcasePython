import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            amount REAL,
            category TEXT,
            description TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_expense(self, date, amount, category, description):
        query = "INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (date, amount, category, description))
        self.conn.commit()
        print("Expense added successfully!")

    def get_expenses(self):
        query = "SELECT * FROM expenses"
        return self.conn.execute(query).fetchall()

    def update_expense(self, id, date, amount, category, description):
        query = "UPDATE expenses SET date=?, amount=?, category=?, description=? WHERE id=?"
        self.conn.execute(query, (date, amount, category, description, id))
        self.conn.commit()
        print("Expense updated successfully!")
        print(f"Updated expense with ID: {id}")

    def delete_expense(self, id):
        query = "DELETE FROM expenses WHERE id=?"
        self.conn.execute(query, (id,))
        self.conn.commit()
        print("Expense deleted successfully!")
        print(f"Deleted expense with ID: {id}")
