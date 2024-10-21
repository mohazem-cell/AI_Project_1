import random

class PuzzleTile:
    def __init__(self, number):
        self.number = number  # The number on the tile

    def __repr__(self):
        return f'{self.number}' if self.number != 0 else ' '  # Display empty space as ' '

class PuzzleBoard:
    def __init__(self, size=3):
        self.size = size  # Size of the puzzle (default 3x3)
        self.board = self.create_board()  # Create the puzzle board matrix
        self.empty_pos = self.find_empty()  # Find the initial position of the empty space

    def make_random(self):
        """
        Create a shuffled puzzle board with tiles numbered from 1 to (size*size - 1)
        and one empty space represented by 0.
        """
        numbers = list(range(self.size * self.size))  # Numbers from 0 to 8 (for 3x3)
        random.shuffle(numbers)  # Shuffle to create a randomized board
        return numbers


    def create_board(self):
        numbers=self.make_random()
        # Create a matrix (2D list) of PuzzleTile objects
        board = [[PuzzleTile(numbers[i * self.size + j]) for j in range(self.size)] for i in range(self.size)]
        return board

    def find_empty(self):
        """
        Find the position of the empty space (tile 0) on the board.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].number == 0:
                    return (i, j)  # Return the row and column of the empty space

    def display_board(self):
        """
        Display the board in a human-readable format.
        """
        empty_postion=self.find_empty()
        print(f'The row number is {empty_postion[0]} and column number is {empty_postion[1]}')
        for row in self.board:
            print(' | '.join(map(str, row)))
            print('-' * (self.size * 4 - 1))  # Divider between rows

# # Example usage
# puzzle = PuzzleBoard(3)  # Create a 3x3 puzzle board
# puzzle.display_board()  # Display the randomized puzzle
