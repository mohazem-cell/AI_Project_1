from queue import PriorityQueue
from create_board import board_puzzle
from heap_queue import heap_queue
from node import node

class Player:
    def __init__(self, puzzle):
        self.puzzle = puzzle  # The puzzle board object

    # def calculate_cost(self):
    #     while self.check_win() and :


    def move(self, direction):
        """
        Moves the empty tile in the specified direction if possible.
        Direction can be 'up', 'down', 'left', 'right'.
        """
        # Get the current position of the empty tile
        
        i = self.puzzle.find_empty()  # Find the current position of the empty space
        if direction == 'up':
            self.move_tile(i, i - 3)  # Move the empty space up
        elif direction == 'down':
            self.move_tile(i, i + 3)  # Move the empty space down
        elif direction == 'left':
            self.move_tile(i, i-1)  # Move the empty space left
        elif direction == 'right':
            self.move_tile(i, i+1)  # Move the empty space right
        else:
            print("Invalid move. Please use 'up', 'down', 'left', or 'right'.")

    def move_tile(self, empty_i, new_i):
        """
        Helper method to move the tile if the move is valid (within bounds).
        """
        # Check if the new position is within the board limits
        if 0 <= new_i < self.puzzle.size:
            # Swap the empty tile (0) with the adjacent tile
            self.puzzle.board[empty_i], self.puzzle.board[new_i] = (
                self.puzzle.board[new_i],
                self.puzzle.board[empty_i],
            )
        # else:
        #     print("Move out of bounds!")

    def check_win(self,board):
        """
        Checks if the puzzle is solved (tiles are in order from 1 to size-1).
        """
        
        for i in range(len(board)):
            if board[i].number != i:
                return False

        return True

    def cost_calculations(self,board):
        """
        to calculte cost of misplaced tiles
        """
        cost = 0
        for i in range(len(board)):
            if board[i].number != i :
                cost+=1
            else:
                continue

        return cost

    def play_bfs(self):
        """
        Implements BFS to solve the puzzle and find the shortest path.
        """
        # Define possible moves
        moves = ['up', 'down', 'left', 'right']
        visited = set()  # To track visited states
        priority_queue=heap_queue() # for bfs
        copy_board=self.puzzle.board.copy()

        # Creating intial node with starting state 
        cost=self.cost_calculations(self.puzzle.board)
        root=node(copy_board,None,cost,0)

        
        priority_queue.push(root)
        
        while not priority_queue.is_empty():

            # Get current node with minmum cost
            min_node=priority_queue.pop()
            current_board=min_node.puzzle

            if self.check_win(current_board):
                return self.get_solution_path(min_node) # return the shortest path solution

            # Mark the current board as visited
            # visited.add(tuple(map(tuple, current_board.board)))
            visited.add(tuple(current_board))

            # To explore all pssible paths to get to the solution
            for move in moves:
                self.puzzle.board=current_board.copy()
                self.move(move)
                new_board=self.puzzle.board.copy()

                # If the new state hasn't been visited
                if tuple(new_board) not in visited:
                    new_cost = self.cost_calculations(new_board)
                    new_node = node(new_board, min_node, new_cost, min_node.level + 1)
                    priority_queue.push(new_node)

        return None

    def get_solution_path(self,node):
        path=[]
        current = node

        while current is not None:
            path.append(current.puzzle)
            current = current.parent

        return path[::-1] # to reverse the order to get the sequence ordered

    # def print_puzz


# Example usage
if __name__ == "__main__":
    puzzle = board_puzzle(9)  # Create a 3x3 puzzle board
    player = Player(puzzle)  # Create a player for the puzzle

    # play(puzzle)
    # Display the initial puzzle
    print("Initial Puzzle:")
    puzzle.display_board()

    # to use BFS to solve the puzzle
    solution_path = player.play_bfs()

    if solution_path:
        print("Puzzle Solved! Here's the sequence of board states:")
        # print("\n")
        for state in solution_path:
            print(state)
    else:
        # print("\n")
        print("No solution found.")
    # # # Player moves
    # while not player.check_win():
    #     move = input("Enter your move (up, down, left, right): ").strip().lower()
    #     player.move(move)
    #     puzzle.display_board()
    #     print(f'{player.cost_calculations()}')

    
    print("\nCongratulations! You solved the puzzle!")