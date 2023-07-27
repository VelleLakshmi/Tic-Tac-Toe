import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = [tk.Button(self.root, text="", font=("Arial", 40), width=4, height=2, command=lambda idx=i: self.on_click(idx)) for i in range(9)]
        self.x_turn = True

        for i in range(9):
            row, col = divmod(i, 3)
            self.buttons[i].grid(row=row, column=col)

    def on_click(self, index):
        button = self.buttons[index]
        if self.x_turn:
            button["text"] = "X"
        else:
            button["text"] = "O"

        button["state"] = tk.DISABLED
        self.x_turn = not self.x_turn
        self.check_for_winner()

    def check_for_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.buttons[i]["text"] == self.buttons[i+1]["text"] == self.buttons[i+2]["text"] and self.buttons[i]["text"] != "":
                messagebox.showinfo("Game Over", f"{self.buttons[i]['text']} wins!")
                self.reset_game()
                return

        # Check columns
        for i in range(3):
            if self.buttons[i]["text"] == self.buttons[i+3]["text"] == self.buttons[i+6]["text"] and self.buttons[i]["text"] != "":
                messagebox.showinfo("Game Over", f"{self.buttons[i]['text']} wins!")
                self.reset_game()
                return

        # Check diagonals
        if self.buttons[0]["text"] == self.buttons[4]["text"] == self.buttons[8]["text"] and self.buttons[0]["text"] != "":
            messagebox.showinfo("Game Over", f"{self.buttons[0]['text']} wins!")
            self.reset_game()
            return

        if self.buttons[2]["text"] == self.buttons[4]["text"] == self.buttons[6]["text"] and self.buttons[2]["text"] != "":
            messagebox.showinfo("Game Over", f"{self.buttons[2]['text']} wins!")
            self.reset_game()
            return

        # Check for tie
        if all(button["text"] != "" for button in self.buttons):
            messagebox.showinfo("Game Over", "Tie game!")
            self.reset_game()

    def reset_game(self):
        for button in self.buttons:
            button["text"] = ""
            button["state"] = tk.NORMAL
        self.x_turn = True

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
