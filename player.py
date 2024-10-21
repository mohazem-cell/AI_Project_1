from create import PuzzleBoard

class Player:
    def __init__(self, puzzle):
        self.puzzle = puzzle  # The puzzle board object

    def move(self, direction):
        """
        Moves the empty tile in the specified direction if possible.
        Direction can be 'up', 'down', 'left', 'right'.
        """
        # Get the current position of the empty tile
        
        i, j = self.puzzle.find_empty()  # Find the current position of the empty space
        if direction == 'up':
            self.move_tile(i, j, i - 1, j)  # Move the empty space up
        elif direction == 'down':
            self.move_tile(i, j, i + 1, j)  # Move the empty space down
        elif direction == 'left':
            self.move_tile(i, j, i, j - 1)  # Move the empty space left
        elif direction == 'right':
            self.move_tile(i, j, i, j + 1)  # Move the empty space right
        else:
            print("Invalid move. Please use 'up', 'down', 'left', or 'right'.")

    def move_tile(self, empty_i, empty_j, new_i, new_j):
        """
        Helper method to move the tile if the move is valid (within bounds).
        """
        # Check if the new position is within the board limits
        if 0 <= new_i < self.puzzle.size and 0 <= new_j < self.puzzle.size:
            # Swap the empty tile (0) with the adjacent tile
            self.puzzle.board[empty_i][empty_j], self.puzzle.board[new_i][new_j] = (
                self.puzzle.board[new_i][new_j],
                self.puzzle.board[empty_i][empty_j],
            )
        else:
            print("Move out of bounds!")

    def check_win(self):
        """
        Checks if the puzzle is solved (tiles are in order from 1 to size*size-1).
        """
        expected = 1
        for i in range(self.puzzle.size):
            for j in range(self.puzzle.size):
                if i == self.puzzle.size - 1 and j == self.puzzle.size - 1:
                    return self.puzzle.board[i][j].number == 0  # The last tile should be the empty tile (0)
                if self.puzzle.board[i][j].number != expected:
                    return False
                expected += 1
        return True

# Example usage
if __name__ == "__main__":
    puzzle = PuzzleBoard(3)  # Create a 3x3 puzzle board
    player = Player(puzzle)  # Create a player for the puzzle

    # Display the initial puzzle
    print("Initial Puzzle:")
    puzzle.display_board()

    # Player moves
    while not player.check_win():
        move = input("Enter your move (up, down, left, right): ").strip().lower()
        player.move(move)
        puzzle.display_board()

    print("Congratulations! You solved the puzzle!")