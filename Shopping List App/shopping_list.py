import tkinter as tk
from tkinter import messagebox, filedialog
#from typing import BinaryIO
import csv
import pickle

class ListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("List")
        self.list = []

    #GUI
        #INPUT
        self.entry = tk.Entry(root, width = 32)
        self.entry.grid(row = 0, column = 0, padx = 10, pady = 10)

        #ADD
        self.add_button = tk.Button(root, text="Add item", command=self.add_item)
        self.add_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        #LIST
        self.listbox = tk.Listbox(root, width = 50, height = 15)
        self.listbox.grid(row=1, column = 0, columnspan = 2, padx = 10, pady = 10)

        #EDIT
        self.edit_button = tk.Button(root, text="Edit item", command= self.edit_item)
        self.edit_button.grid(row = 2, column = 0, pady = 10)

        #DEL
        self.delete_button = tk.Button(root, text="Delete item", command=self.delete_item)
        self.delete_button.grid(row = 2, column = 1, pady = 10)

        #SAVE_CSV
        self.save_button = tk.Button(root, text="Save to CSV", command=self.save_csv)
        self.save_button.grid(row = 3, column = 0, pady = 10)

        #LOAD_CSV
        self.load_button = tk.Button(root, text="Load from CSV", command=self.load_csv)
        self.load_button.grid(row = 3, column = 1, pady = 10)

        #SAVE_PICKLE
        self.save_pickle_button = tk.Button(root, text="Save to Pickle", command=self.save_pickle)
        self.save_pickle_button.grid(row = 4, column = 0, pady = 10)

        #LOAD_PICKLE
        self.load_pickle_button = tk.Button(root, text="Load from Pickle", command=self.load_pickle)
        self.load_pickle_button.grid(row = 4, column = 1, pady = 10)

        #SAVE_JSON

        #LOAD_JSON


    def add_item(self):
        item = self.entry.get()
        if item:
            self.list.append(item)
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Cannot add empty value.")

    def edit_item(self):
        try:
            index = self.listbox.curselection()[0]
            new_value = self.entry.get()
            if new_value:
                self.list[index] = new_value
                self.listbox.delete(index)
                self.listbox.insert(index, new_value)
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Error", "Cannot set empty value.")
        except IndexError:
            messagebox.showwarning("Error", "Choose item to edit.")

    def delete_item(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            del self.list[index]
        except IndexError:
            messagebox.showwarning("Error", "Choose item to delete.")

    def save_csv(self):
        file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if file:
            with open(file, "w", newline="") as f:
                writer = csv.writer(f)
                for item in self.list:
                    writer.writerow([item])
            messagebox.showinfo("Saved", "List has been saved to CSV file.")

    def load_csv(self):
        file = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if file:
            with open(file, "r") as f:
                reader = csv.reader(f)
                self.list = [row[0] for row in reader]
                self.listbox.delete(0, tk.END)
                for item in self.list:
                    self.listbox.insert(tk.END, item)
            messagebox.showinfo("Loaded", "List has been loaded from CSV file.")

    def save_pickle(self):
        file = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle", "*.pkl")])
        if file:
            with open(file, "wb") as f:
                #f : BinaryIO
                pickle.dump(self.list, f)
            messagebox.showinfo("Saved", "List has been saved to Pickle file.")

    def load_pickle(self):
        file = filedialog.askopenfilename(filetypes=[("Pickle", "*.pkl")])
        if file:
            with open(file, "rb") as f:
                self.list = pickle.load(f)
                self.listbox.delete(0, tk.END)
                for item in self.list:
                    self.listbox.insert(tk.END, item)
            messagebox.showinfo("Loaded", "List has been loaded from Pickle file.")



if __name__ == "__main__":
    root = tk.Tk()
    app = ListApp(root)
    root.mainloop()

