"""
Qubic
~~~~~

Author: 
Description: Game tree
"""
import const

class Node:
    """A node class for game tree."""
    
    def __init__(self):

        self.field = [[[0, 0, 0]*3]*3]
        self.childs = []
        self.win = 0
        self.player = False
        

    ...


class Tree:
    """A game tree class."""
    
    def __init__(self):
        self.tree = Node()


    def build(self, max_height: int, player: bool):
        """Extetree structure."""
        
        self.build(self, self.tree, max_height, player)

    def build_(self, node, max_height, player):
        
        if max_height == 0:
            return 

        for y in range(3):

            for x in range(3):

                for z in range(3):
                    
                    if node.field[y][x][z] == 0:
                        child = Node()
                        child.field = node.field
                        node.childs += [child]

                        if player == True:
                            child.field[y][x][z] = const.CROSS 

                        else:
                            child.field[y][x][z] = const.CIRCLE
                        
                        child.player = player

                        self.build_(child, max_height-1, not player)

    
    def evaluate(self):
        """Rate the win pos."""

        # self.negamax() -> end
        # self.rate() -> open

        
    
    def rateNegamax(self):
        """Rate by negamax."""

        self.rateNegamax_(self.tree)

    def rateNegamax_(self, node: Node):
        
        if not node.childs:
            
            if self.countZero(node) == 0:
                
                if node.player == True:

                    if self.checkWin(node) == True:
                        node.win = +1
                    
                    else:
                        node.win = -1
                
                else:
                    node.win = 0
            
            else:
                self.rateCustom(node)


        maxi = -1
        
        for child in node.childs:

            win = -self.rateNegamax_(child)

            if win > maxi:
                maxi = win

        node.win = maxi

        return maxi


    def rateCustom(self, node: Node):
        """Rate by custom rating."""

        
    
    def checkWin(self, node: Node):
        """Check a pos for a win."""
            # z, y, x
        list_win = [
            ((0, 0, 0),(0, 0, 1),(0, 0, 2)), # Layer 0 von vorn
            ((0, 1, 0),(0, 1, 1),(0, 1, 2)),
            ((0, 2, 0),(0, 2, 1),(0, 2, 2)),
            ((0, 0, 0),(0, 1, 0),(0, 2, 0)),
            ((0, 0, 1),(0, 1, 1),(0, 2, 1)),
            ((0, 0, 2),(0, 1, 2),(0, 2, 2)),
            ((0, 0, 0),(0, 1, 1),(0, 2, 2)),
            ((0, 0, 2),(0, 1, 1),(0, 2, 0)),
            
            ((1, 0, 0),(1, 0, 1),(1, 0, 2)), # Layer 1 von vorn
            ((1, 1, 0),(1, 1, 1),(1, 1, 2)),
            ((1, 2, 0),(1, 2, 1),(1, 2, 2)),
            ((1, 0, 0),(1, 1, 0),(1, 2, 0)),
            ((1, 0, 1),(1, 1, 1),(1, 2, 1)),
            ((1, 0, 2),(1, 1, 2),(1, 2, 2)),
            ((1, 0, 0),(1, 1, 1),(1, 2, 2)),
            ((1, 0, 2),(1, 1, 1),(1, 2, 0)),
            
            ((2, 0, 0),(2, 0, 1),(2, 0, 2)), # Layer 2 von vorn
            ((2, 1, 0),(2, 1, 1),(2, 1, 2)),
            ((2, 2, 0),(2, 2, 1),(2, 2, 2)),
            ((2, 0, 0),(2, 1, 0),(2, 2, 0)),
            ((2, 0, 1),(2, 1, 1),(2, 2, 1)),
            ((2, 0, 2),(2, 1, 2),(2, 2, 2)),
            ((2, 0, 0),(2, 1, 1),(2, 2, 2)),
            ((2, 0, 2),(2, 1, 1),(2, 2, 0)),
            
            ((0, 0, 0),(1, 0, 0),(2, 0, 0)), # Layerübergreifend längs
            ((0, 0, 1),(1, 0, 1),(2, 0, 1)),
            ((0, 0, 2),(1, 0, 2),(2, 0, 2)),
            ((0, 1, 0),(1, 1, 0),(2, 1, 0)),
            ((0, 1, 1),(1, 1, 1),(2, 1, 1)),
            ((0, 1, 2),(1, 1, 2),(2, 1, 2)),
            ((0, 2, 0),(1, 2, 0),(2, 2, 0)),
            ((0, 2, 1),(1, 2, 1),(2, 2, 1)),
            ((0, 2, 2),(1, 2, 2),(2, 2, 2)),

        
            ((0, 0, 0),(1, 1, 1),(2, 2, 2)), # Raumdiagonalen
            ((2, 0, 0),(1, 1, 1),(0, 2, 2)),
            ((2, 0, 2),(1, 1, 1),(0, 2, 0)),
            ((0, 0, 2),(1, 1, 1),(2, 2, 0)),
            ((0, 0, 0),(1, 1, 0),(2, 2, 0)),
            ((0, 0, 1),(1, 1, 1),(2, 2, 1)),
            ((0, 0, 2),(1, 1, 2),(2, 2, 2)),
            ((0, 2, 0),(1, 1, 0),(2, 0, 0)),
            ((0, 2, 1),(1, 1, 1),(2, 0, 1)),
            ((0, 2, 2),(1, 1, 2),(2, 0, 2)),
        ]
    
        for win in list_win:

            if (node.field[win[0][0]][win[0][1]][win[0][2]]
                == node.field[win[1][0]][win[1][1]][win[1][2]]
                == node.field[win[2][0]][win[2][1]][win[2][2]]):

                if node.field[win[0][0]][win[0][1]][win[0][2]] != const.EMPTY:
                    return True
        
        return False

   
    def checkDraw(self, node: Node):
        """Check a pos for a draw."""

        if self.checkWin(node) == False:
            return True
        
        return False
    

    def countZero(self, node):

        zero = 0

        for x in range(3):
            
            for y in range(3):
                
                for z in range(3):

                    if node.field[x][y][z] == 0:
                        zero += 1

        return zero