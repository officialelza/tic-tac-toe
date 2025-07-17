# Tic-Tac-Toe Game | Created by Aleena Elza Mathew

This project is a simple implementation of the classic Tic-Tac-Toe game using Python and Pygame. It allows two players to play against each other on a graphical interface.

---

## Features

1. **Graphical User Interface (GUI)**: A visually appealing 3x3 grid.
2. **Two-Player Mode**: Alternate turns between Player 1 and Player 2.
3. **Winner Detection**: Automatically detects and announces the winner.
4. **Play Again Option**: Restart the game after a winner is declared.
5. **Draw Handling**: Detects when the board is full without a winner.
6. **Customizable Colors and Fonts**: Modify the game's appearance easily.

---

## Installation

1. Ensure Python is installed on your system.
2. Install the Pygame library if not already installed:
   ```
   pip install pygame
   ```
3. Download or clone the repository to your local machine.

---

## How to Run

1. Navigate to the project folder in your terminal.
2. Run the game script:
   ```
   python tic_tac_toe.py
   ```
3. The game window will open, and you can start playing.

---

## Gameplay Instructions

1. The grid is displayed as a 3x3 board.
2. Player 1 uses "X" (yellow lines), and Player 2 uses "O" (red circles).
3. Click on an empty cell to make your move.
4. The game will announce the winner or declare a draw if the board is full.
5. To play again, click the "Play Again?" button after the game ends.

---

## File Details

- **tic_tac_toe.py**: The main Python script containing the game logic.
- **sauce.otf**: Custom font file used for text rendering.
- **cat.gif**: A celebratory image displayed when a player wins.

---

## Code Highlights

1. **Grid Drawing**:
   The grid is drawn using `pygame.draw.line` to create horizontal and vertical lines.

2. **Winner Detection**:
   The game checks for three consecutive marks (row, column, or diagonal) to determine the winner.

3. **Replay Mechanism**:
   Players can reset the game using the "Play Again?" button.

4. **Dynamic Drawing**:
   Player moves ("X" or "O") are dynamically drawn on the grid using the mouse click position.

---

## Future Enhancements

1. Add an AI opponent for single-player mode.
2. Enhance the UI with animations and sounds.
3. Track player scores across multiple rounds.

---

## Acknowledgments

- Created with Python and Pygame.
- Fonts and images are customized for better user experience.

---

