# gui.py

import tkinter as tk
from tkinter import messagebox
from solver import solve


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.configure(bg="#dfe6ee")

        self.entries = []
        self.original_cells = set()

        title = tk.Label(
            root,
            text="Sudoku Solver",
            font=("Helvetica", 24, "bold"),
            bg="#dfe6ee",
            fg="#2f3e56",
            pady=10,
        )
        title.grid(row=0, column=0, columnspan=9)

        self.create_grid()
        self.create_buttons()

    def create_grid(self):

        board_frame = tk.Frame(
            self.root,
            bg="#2f3e56",
            bd=4,
        )

        board_frame.grid(row=1, column=0, columnspan=9, padx=20, pady=20)

        for row in range(9):

            row_entries = []

            for col in range(9):

                # Thicker borders every 3 cells
                top = 3 if row % 3 == 0 else 1
                left = 3 if col % 3 == 0 else 1
                bottom = 3 if row == 8 else 1
                right = 3 if col == 8 else 1

                cell_frame = tk.Frame(
                    board_frame,
                    bg="#2f3e56",
                    highlightbackground="#2f3e56",
                    highlightcolor="#2f3e56",
                    highlightthickness=0,
                )

                cell_frame.grid(
                    row=row,
                    column=col,
                    padx=(left, right),
                    pady=(top, bottom),
                )

                entry = tk.Entry(
                    cell_frame,
                    width=2,
                    font=("Helvetica", 24),
                    justify="center",
                    bd=0,
                    relief="flat",
                    bg="#f4f4f4",
                    fg="#2f3e56",
                )

                entry.pack(ipady=10)

                # Arrow navigation
                entry.bind(
                    "<Up>",
                    lambda e, r=row, c=col: self.move_focus(r - 1, c)
                )

                entry.bind(
                    "<Down>",
                    lambda e, r=row, c=col: self.move_focus(r + 1, c)
                )

                entry.bind(
                    "<Left>",
                    lambda e, r=row, c=col: self.move_focus(r, c - 1)
                )

                entry.bind(
                    "<Right>",
                    lambda e, r=row, c=col: self.move_focus(r, c + 1)
                )

                row_entries.append(entry)

            self.entries.append(row_entries)

    # def create_grid(self):
    #     frame = tk.Frame(self.root, bg="#2f3e56")
    #     frame.grid(row=1, column=0, columnspan=9, padx=20, pady=20)

    #     for row in range(9):
    #         row_entries = []

    #         for col in range(9):
    #             entry = tk.Entry(
    #                 frame,
    #                 width=2,
    #                 font=("Helvetica", 24),
    #                 justify="center",
    #                 bd=0,
    #                 relief="flat",
    #                 bg="#f4f4f4",
    #                 fg="#2f3e56",
    #             )

    #             padx = (2 if col % 3 == 0 else 1)
    #             pady = (2 if row % 3 == 0 else 1)

    #             entry.grid(
    #                 row=row,
    #                 column=col,
    #                 padx=padx,
    #                 pady=pady,
    #                 ipady=10,
    #             )

    #             # Arrow key movement
    #             entry.bind("<Up>", lambda e, r=row, c=col: self.move_focus(r - 1, c))
    #             entry.bind("<Down>", lambda e, r=row, c=col: self.move_focus(r + 1, c))
    #             entry.bind("<Left>", lambda e, r=row, c=col: self.move_focus(r, c - 1))
    #             entry.bind("<Right>", lambda e, r=row, c=col: self.move_focus(r, c + 1))

    #             row_entries.append(entry)

    #         self.entries.append(row_entries)

    def move_focus(self, row, col):
        if 0 <= row < 9 and 0 <= col < 9:
            self.entries[row][col].focus_set()

    def validate_initial_board(self, board):
        invalid_cells = []

        for row in range(9):
            for col in range(9):

                num = board[row][col]

                if num == 0:
                    continue

                # Temporarily remove number
                board[row][col] = 0

                if not self.is_valid_position(board, row, col, num):
                    invalid_cells.append((row, col))

                # Restore number
                board[row][col] = num

        return invalid_cells

    def is_valid_position(self, board, row, col, num):

        # Row check
        for x in range(9):
            if board[row][x] == num:
                return False

        # Column check
        for x in range(9):
            if board[x][col] == num:
                return False

        # 3x3 box check
        start_row = row - row % 3
        start_col = col - col % 3

        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def get_board(self):
        board = []
        self.original_cells.clear()

        for row in range(9):
            current_row = []

            for col in range(9):
                value = self.entries[row][col].get()

                if value == "":
                    current_row.append(0)
                else:
                    try:
                        number = int(value)

                        if number < 1 or number > 9:
                            raise ValueError

                        current_row.append(number)

                        self.original_cells.add((row, col))

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

                # Original user numbers = black
                if (row, col) in self.original_cells:
                    self.entries[row][col].config(
                        fg="#160a08",
                        disabledforeground="#160a08",
                    )

                # Solved numbers = blue
                else:
                    self.entries[row][col].config(
                        fg="#2e5aac",
                        disabledforeground="#2e5aac",
                    )

    def solve_puzzle(self):

        # Reset colors first
        for row in self.entries:
            for entry in row:
                entry.config(bg="#f4f4f4")

        board = self.get_board()

        if board is None:
            return

        # Validate initial board
        invalid_cells = self.validate_initial_board(board)

        if invalid_cells:

            for row, col in invalid_cells:
                self.entries[row][col].config(bg="#ffb3b3")

            messagebox.showerror(
                "Invalid Sudoku",
                "Initial board is invalid.\nWrong cells are highlighted in red.",
            )

            return

        if solve(board):
            self.update_board(board)
        else:
            messagebox.showerror(
                "No Solution",
                "This Sudoku puzzle cannot be solved.",
            )

    def clear_board(self):
        self.original_cells.clear()

        for row in self.entries:
            for entry in row:

                # Reset text color
                entry.config(
                    fg="#2f3e56",
                    bg="#f4f4f4",
                )

                # Clear value
                entry.delete(0, tk.END)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#dfe6ee")
        button_frame.grid(row=2, column=0, columnspan=9, pady=10)

        solve_button = tk.Button(
            button_frame,
            text="Solve",
            command=self.solve_puzzle,
            font=("Helvetica", 14, "bold"),
            bg="#4f81c7",
            fg="white",
            activebackground="#3f6cab",
            padx=20,
            pady=10,
            bd=0,
            cursor="hand2",
        )

        solve_button.grid(row=0, column=0, padx=10)

        clear_button = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_board,
            font=("Helvetica", 14, "bold"),
            bg="#c94f4f",
            fg="white",
            activebackground="#a63e3e",
            padx=20,
            pady=10,
            bd=0,
            cursor="hand2",
        )

        clear_button.grid(row=0, column=1, padx=10)