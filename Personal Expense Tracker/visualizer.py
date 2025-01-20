import matplotlib.pyplot as plt

class ExpenseVisualizer:
    def __init__(self):
        pass

    plt.rcParams.update({'font.size': 12})
    def plot_expenses_by_category(self, summary):
        #Unpack dict & keys
        categories = list(summary.keys())
        amounts = list(summary.values())
        plt.bar(categories, amounts, color="skyblue")
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

    def plot_expenses_over_time(self, expenses):
        expenses = expenses.sort_values(by="date")
        dates = expenses["date"]
        amounts = expenses["amount"]
        plt.plot(dates, amounts, marker ='o', linestyle="-", color="green")
        plt.title("Expenses Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)
        plt.show()

    def plot_expenses_pie_chart(self, summary):
        categories = list(summary.keys())
        amounts = list(summary.values())
        plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        plt.title("Expenses by Category")
        plt.show()











    def plot_monthly_expenses(self, expenses):
        #TODO - matplotlib to plot
        pass