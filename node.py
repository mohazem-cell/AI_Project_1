from create_board import board_puzzle

class node:
    def __init__(self,puzzle,parent,cost,level):
        self.puzzle=puzzle
        self.parent=parent
        self.cost=cost
        self.level=level
    
    def __lt__(self,nxt) ->bool:
        return self.cost < nxt.cost