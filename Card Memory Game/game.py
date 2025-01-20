import tkinter as tk
import random
import time
from typing import List



class CardMemoryGame:
    def __init__(self, root, n = 8):
        self.root = root
        self.n = n
        self.grid = self.initialize_game()
        self.revealed = [[False] * n for _ in range(n)]
        self.buttons = [[None] * n for _ in range(n)]
        self.first_card = None
        self.start_time = None

        self.create_widgets()

    def initialize_game(self):
        #Pairs and shuffle
        num_pairs = (self.n * self.n) // 2
        card_val = list(range(1, num_pairs + 1)) * 2
        random.shuffle(card_val)

        #Grid
        return [card_val[i * self.n:(i + 1) * self.n] for i in range(self.n)]

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.info_label = tk.Label(self.root, text="Click 'Start' to begin!", font=("Arial", 14))
        self.info_label.pack(pady=10)

        #START
        self.start_button = tk.Button(self.root, text= "Start", command=self.start_game, font=("Arial", 12))
        self.start_button.pack(pady=10)


    def start_game(self):
        self.start_time = time.time()
        self.info_label.config(text="Find all the matching pairs!")
        self.start_button.pack_forget() #Hide Button

        #Grid
        for i in range(self.n):
            for j in range(self.n):
                button = tk.Button(self.frame, text="*", width=5, height=2,
                                   command=lambda row=i, col=j: self.reveal_card(row,col))
                button.grid(row = i, column = j, padx=5, pady=5)
                self.buttons[i][j] = button


    def reveal_card(self, row, col):
        if self.revealed[row][col]:
            return

        #Reveal
        self.revealed[row][col] = True
        self.buttons[row][col].config(text=str(self.grid[row][col]))

        if not self.first_card:
            self.first_card = (row, col)
        else:
            row1, col1 = self.first_card
            row2, col2 = row,col
            self.root.after(500, self.check_match, row1, col1, row2, col2)
            self.first_card = None


    def check_match(self, row1, col1, row2, col2):
        if self.grid[row1][col1] == self.grid[row2][col2]:
            #When matched
            self.buttons[row1][col1].config(state="disabled", disabledforeground="black")
            self.buttons[row2][col2].config(state="disabled", disabledforeground="black")
            self.info_label.config(text="It's a match!")
        else:
            #No match - reset
            self.revealed[row1][col1] = False
            self.revealed[row2][col2] = False
            self.buttons[row1][col1].config(text="*")
            self.buttons[row2][col2].config(text="*")
            self.info_label.config(text="No match!")

        if self.all_matched():
            end_time = time.time()
            elapsed_time = round(end_time - self.start_time, 2)
            self.info_label.config(text=f"Congratz! You finished in {elapsed_time} seconds.")
            self.show_restart_button()


    def all_matched(self):
        return all(all(row) for row in self.revealed)

    def show_restart_button(self):
        if not hasattr(self, "restart_button"):
            self.restart_button = tk.Button(self.root, text="Restart", font=("Arial",12), command=self.restart_game)
            self.restart_button.pack(pady=10)

    def restart_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.grid = self.initialize_game()
        self.revealed = [[False] * self.n for _ in range(self.n)]
        self.buttons = [[None] * self.n for _ in range(self.n)]
        self.first_card = None
        self.start_time = None

        self.create_widgets()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Card Memory Game")
    app = CardMemoryGame(root, n=8)
    root.mainloop()