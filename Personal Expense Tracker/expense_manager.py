import pandas as pd

class ExpenseManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_expense(self, date, amount, category, description):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.db_manager.add_expense(date, amount, category, description)

    def get_expenses_as_dataframe(self):
        data = self.db_manager.get_expenses()
        df = pd.DataFrame(data, columns=["ID", "Date", "Amount", "Category", "Description"])
        df["Date"] = pd.to_datetime(df["Date"])
        return df

    def filter_expenses(self, category=None, start_date=None, end_date=None):
        df = self.get_expenses_as_dataframe()
        if category:
            df = df[df["Category"] == category]
        if start_date:
            df = df[df["Date"] >= pd.to_datetime(start_date)]
        if end_date:
            df = df[df["Date"] <= pd.to_datetime(end_date)]
        return df

    def calculate_summary(self):
        df = self.get_expenses_as_dataframe()
        summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
        return summary

    def calculate_monthly_summary(self):
        df = self.get_expenses_as_dataframe()
        df["Month"] = df["Date"].dt.to_period("M")
        return df.groupby("Month")["Amount"].sum()

    def get_summary_to_dict(self):
        summary = self.calculate_summary()
        return summary.to_dict()
