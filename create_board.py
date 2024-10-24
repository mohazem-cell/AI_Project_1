import random

class _tile_puzzle:
    def __init__(self,number):
        self.number=number
    
    def __repr__(self) -> str:
        return f'{self.number}' if self.number !=0 else ' '

class board_puzzle:
    def __init__(self,size) :
        self.size=size
        self.board=self.create_board()
        self.empty_postion=self.find_empty()

    
    def make_random(self):
        numbers = list(range(self.size))  # Numbers from 0 to 8 for 1D array
        random.shuffle(numbers)  # Shuffle to create a randomized board
        return numbers
    
    def create_board(self):
        numbers=self.make_random()
        # Ensure that numbers has enough elements
        if len(numbers) < self.size:
            raise ValueError(f"Not enough elements in numbers. Expected at least {self.size}, got {len(numbers)}.")
   
        board = [_tile_puzzle(numbers[i]) for i in range(self.size)]
        return board

    def find_empty(self):
        """
        Find the position of the empty space (tile 0) on the board.
        """
        for i in range(self.size):
                if self.board[i].number == 0:
                    return (i)  # Return the row and column of the empty space

    def display_board(self):
        """
        Display the board in a human-readable format.
        Prints the board with grid lines to separate rows and columns.
        """
        empty_position = self.find_empty()

        # Iterate over the rows of the board
        for i in range(self.size):
            row = self.board[i]  # Get the current row
            b_row=self.board[i-1]
            if str(b_row) in {' ','1', '2', '3', '4', '5', '6', '7', '8'}:
                print(f'| {row} | ', end='')  # Print valid row followed by a separator

            # Print a separator after each row except the last
            if (i-2)%3==0:
                print()
                print('-' * (self.size + 8))  # Dynamic separator based on size
# # test code
# puzzle = board_puzzle(9)  # Create a 3x3 puzzle board
# puzzle.display_board()  # Display the randomized puzzle