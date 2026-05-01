# gui.py

import tkinter as tk
from tkinter import messagebox
from solver import solve


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.configure(bg="#1e1e1e")

        self.entries = []

        title = tk.Label(
            root,
            text="Sudoku Solver",
            font=("Helvetica", 24, "bold"),
            bg="#1e1e1e",
            fg="white",
            pady=10,
        )
        title.grid(row=0, column=0, columnspan=9)

        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.grid(row=1, column=0, columnspan=9, padx=20, pady=20)

        for row in range(9):
            row_entries = []

            for col in range(9):
                entry = tk.Entry(
                    frame,
                    width=2,
                    font=("Helvetica", 20),
                    justify="center",
                    bd=2,
                    relief="ridge",
                    bg="#ffffff",
                )

                padx = (4 if col % 3 == 0 else 1)
                pady = (4 if row % 3 == 0 else 1)

                entry.grid(row=row, column=col, padx=padx, pady=pady, ipady=8)

                row_entries.append(entry)

            self.entries.append(row_entries)

    def get_board(self):
        board = []

        for row in range(9):
            current_row = []

            for col in range(9):
                value = self.entries[row][col].get()

                if value == "":
                    current_row.append(0)
                else:
                    try:
                        current_row.append(int(value))
                    except ValueError:
                        messagebox.showerror(
                            "Invalid Input",
                            "Only numbers 1-9 are allowed",
                        )
                        return None

            board.append(current_row)

        return board

    def update_board(self, board):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(board[row][col]))

    def solve_puzzle(self):
        board = self.get_board()

        if board is None:
            return

        if solve(board):
            self.update_board(board)
        else:
            messagebox.showerror(
                "No Solution",
                "This Sudoku puzzle cannot be solved",
            )

    def clear_board(self):
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)

    def create_buttons(self):
        solve_button = tk.Button(
            self.root,
            text="Solve",
            command=self.solve_puzzle,
            font=("Helvetica", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
        )

        solve_button.grid(row=2, column=2, columnspan=2, pady=10)

        clear_button = tk.Button(
            self.root,
            text="Clear",
            command=self.clear_board,
            font=("Helvetica", 14, "bold"),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
        )

        clear_button.grid(row=2, column=5, columnspan=2, pady=10)

