from math import sqrt
from create_board import board_puzzle
from heap_queue import heap_queue
from node import node
from collections import deque

class Player:
    def __init__(self, puzzle):
        self.puzzle = puzzle  # The puzzle board object

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
            if i%3==0:
                return
            else:
                self.move_tile(i, i-1)  # Move the empty space left
        elif direction == 'right':
            if (i-2)%3==0:
                return
            else:
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


    def Manhattan_distance(self,board):
        """
        Calculate the Manhattan distance of the puzzle.
        """
        distance = 0
        for i in range(len(board)):
            if board[i].number != 0:
                correct_postion=board[i].number
                current_row,current_col=divmod(i,3)
                new_row,new_col=divmod(correct_postion,3)
                distance+=abs(current_row-new_row)+abs(current_col-new_col)
        return distance

    def play_A_star_manhatten(self):
        """
        Play the game using A* algorithm using manhatten hueristics.
        """
        # Define possible moves
        moves = ['up', 'down', 'left', 'right']
        visited = set()  # To track visited states
        priority_queue=heap_queue() # for A star
        copy_board=self.puzzle.board.copy()

        # Creating intial node with starting state 
        cost_manhatten=self.Manhattan_distance(copy_board)
        root=node(copy_board,None,cost_manhatten,0)

        priority_queue.enqueue(root)
        expanded_nodes_manhatten=0

        while not priority_queue.is_empty():

            # Get current node with minmum cost
            goal_node=priority_queue.dequeue()
            current_board=goal_node.puzzle
            expanded_nodes_manhatten+=1

            if self.check_win(current_board):
                print(f'The number of explored nodes in A* using manhatten distance is {expanded_nodes_manhatten}')
                return self.get_solution_path(goal_node) # return the path solution

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
                    level_new=goal_node.level+1  #g(n)
                    hueristics=self.Manhattan_distance(new_board)   #h(n)
                    total_cost=level_new+hueristics    #f(n)=g(n)+h(n)
                    new_node = node(new_board, goal_node, total_cost, level_new)
                    priority_queue.enqueue(new_node)
        return None

    def Euclidean_distance(self,board):
        """
        Calculate the Manhattan distance of the puzzle.
        """
        distance = 0
        for i in range(len(board)):
            if board[i].number != 0:
                correct_postion=board[i].number
                current_row,current_col=divmod(i,3)
                new_row,new_col=divmod(correct_postion,3)
                distance+=sqrt((current_row-new_row) ** 2 + (current_col-new_col) ** 2)
        return distance

    def play_A_star_Euclidean(self):
        """
        Play the game using A* algorithm using manhatten hueristics.
        """
        # Define possible moves
        moves = ['up', 'down', 'left', 'right']
        visited = set()  # To track visited states
        priority_queue=heap_queue() # for A star
        copy_board=self.puzzle.board.copy()

        # Creating intial node with starting state 
        cost_eculidean=self.Manhattan_distance(copy_board)
        root=node(copy_board,None,cost_eculidean,0)

        priority_queue.enqueue(root)
        expanded_nodes_eculidean=0

        while not priority_queue.is_empty():

            # Get current node with minmum cost
            goal_node=priority_queue.dequeue()
            current_board=goal_node.puzzle
            expanded_nodes_eculidean+=1

            if self.check_win(current_board):
                print(f'The number of explored nodes in A* using eculidean distance is {expanded_nodes_eculidean}')
                return self.get_solution_path(goal_node) # return the path solution

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
                    level_new=goal_node.level+1  #g(n)
                    hueristics=self.Euclidean_distance(new_board)   #h(n)
                    total_cost=level_new+hueristics    #f(n)=g(n)+h(n)
                    new_node = node(new_board, goal_node, total_cost, level_new)
                    priority_queue.enqueue(new_node)
        return None

    def play_bfs(self):
        """
        Implements BFS to solve the puzzle.
        """
        # Define possible moves
        moves = ['up', 'down', 'left', 'right']
        visited = set()  # To track visited states
        queue=deque() # queue for bfs
        copy_board=self.puzzle.board.copy()

        # Creating intial node with starting state 
        root=node(copy_board,None,0,0)

        queue.append(root)
        expanded_nodes=0

        while queue:

            # Get current node with minmum cost
            goal_node=queue.popleft()
            current_board=goal_node.puzzle
            expanded_nodes+=1

            if self.check_win(current_board):
                print(f'The number of explored nodes in BFS is {expanded_nodes}')
                return self.get_solution_path(goal_node) # return the path solution

            # Mark the current board as visited
            visited.add(tuple(current_board))

            # To explore all pssible paths to get to the solution
            for move in moves:
                self.puzzle.board=current_board.copy()
                self.move(move)
                new_board=self.puzzle.board.copy()

                # If the new state hasn't been visited
                if tuple(new_board) not in visited:
                    # new_cost = self.cost_calculations(new_board)
                    new_node = node(new_board, goal_node, 0, goal_node.level + 1)
                    queue.append(new_node)
        return None

    def get_solution_path(self,node):
        path=[]
        current = node

        while current is not None:
            path.append(current.puzzle)
            current = current.parent

        return path[::-1] # to reverse the order to get the sequence ordered




# Example usage
if __name__ == "__main__":
    puzzle = board_puzzle(9)  # Create a 3x3 puzzle board
    player = Player(puzzle)  # Create a player for the puzzle

    # play(puzzle)
    # Display the initial puzzle
    print("Initial Puzzle:")
    puzzle.display_board()

    # to use BFS to solve the puzzle
    solution_bfs = player.play_bfs()

    # if solution_bfs:
    #     print("Puzzle Solved! In BFS:")
    #     count=0
    #     # print("\n")
    #     for state in solution_bfs:
    #         for tile in state:
    #             print(f'| {tile.number} | ',end="")
    #             if (count-2)%3==0:
    #                 print("")
    #                 print("-----------------")
    #             # print()
    #             count+=1
    #         print("")
    #     count=0
        
    # else:
    #     # print("\n")
    #     print("No solution found.")

    puzzle1 = board_puzzle(9)  # Create a 3x3 puzzle board
    player1 = Player(puzzle1)  # Create a player for the puzzl
    # to use A* using manhatten to solve the puzzle
    solution_A_star=player1.play_A_star_manhatten()
    # if solution_A_star:
    #     print("Puzzle Solved! In A* search:")
    #     count=0
    #     # print("\n")
    #     for state in solution_A_star:
    #         for tile in state:
    #             print(f'| {tile.number} | ',end="")
    #             if (count-2)%3==0:
    #                 print("")
    #                 print("-----------------")
    #             # print()
    #             count+=1
    #         print("")
    #     count=0
        
    # else:
    #     # print("\n")
    #     print("No solution found.")
    # Player moves
    # while not player.check_win():
    #     move = input("Enter your move (up, down, left, right): ").strip().lower()
    #     player.move(move)
    #     puzzle.display_board()
    #     # print(f'{player.cost_calculations(puzzle)}')

    puzzle2 = board_puzzle(9)  # Create a 3x3 puzzle board
    player2 = Player(puzzle2)  # Create a player for the puzzl
    # to use A* using manhatten to solve the puzzle
    solution_A_star=player2.play_A_star_Euclidean()

    # print("\nCongratulations! You solved the puzzle!")