# Sudoku Solver

A modern Sudoku Solver built with Python and Tkinter featuring an interactive 9x9 graphical interface, real-time validation, keyboard navigation, and a fast recursive backtracking algorithm.

---

## Preview

This application allows users to:

* Enter Sudoku puzzles directly into a graphical 9x9 board
* Navigate between cells using arrow keys
* Detect invalid starting boards automatically
* Highlight incorrect inputs visually
* Solve puzzles instantly
* Clear and restart the board easily

---

# Features

## Interactive GUI

* Clean modern Sudoku interface
* Responsive 9x9 board
* Smooth keyboard navigation with arrow keys

## Smart Validation

* Detects invalid Sudoku configurations
* Highlights incorrect cells in red
* Prevents impossible puzzles from being solved

## Fast Sudoku Solver

* Recursive backtracking algorithm
* Efficient and accurate solving
* Supports standard 9x9 Sudoku puzzles

## User Experience

* Original user numbers displayed in black
* Solver-generated numbers displayed in blue
* Simple and intuitive controls

---

# Technologies Used

* Python 3
* Tkinter GUI Framework
* Recursive Backtracking Algorithm
* Object-Oriented Programming

---

# Project Structure

```text
sudoku-solver/
│
├── main.py
├── gui.py
├── solver.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sudoku-solver.git
```

## 2. Enter the Project Folder

```bash
cd sudoku-solver
```

## 3. Run the Application

```bash
python main.py
```

---

# How to Use

1. Enter the known Sudoku numbers into the board
2. Use arrow keys to move between cells
3. Press the **Solve** button
4. The solved Sudoku appears instantly
5. If the puzzle is invalid, incorrect cells are highlighted

---

# Algorithm

The solver uses a classic recursive backtracking algorithm.

The algorithm:

1. Finds an empty cell
2. Tries numbers from 1–9
3. Validates each move
4. Recursively continues
5. Backtracks when necessary

This guarantees a valid solution for solvable Sudoku puzzles.

---

# Future Improvements

* Animated solving visualization
* Random puzzle generator
* Difficulty selector
* Timer system
* Hint functionality
* Dark/Light mode
* Web application version
* OCR image recognition
* AI-assisted solving heuristics

---

# Author

Built with Python as a personal project focused on algorithms, GUI development, and problem solving.

---

# License

This project is open-source and available under the MIT License.
