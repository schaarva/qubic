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

        self.field = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ] # BUG
        self.childs = []
        self.win = 0
        self.player = False


class Tree:
    """A game tree class."""
    
    def __init__(self):
        self.tree = Node()


    def build(self, max_height: int, player: bool):
        """Extetree structure."""
        
        self._build(self.tree, max_height, player)

    def _build(self, node: Node, max_height: int, player: bool):
        
        if max_height == 0:
            return 

        for y in range(3):

            for x in range(3):

                for z in range(3):
                    
                    if node.field[y][x][z] == const.EMPTY:
                        child = Node()
                        child.field = node.field
                        node.childs += [child]
                        
                        if player == True:
                            child.field[y][x][z] = const.CROSS 

                        else:
                            child.field[y][x][z] = const.CIRCLE
                        
                        child.player = player

                        self._build(child, max_height-1, not player)
    
    def countNodes(self):
        return self._countNodes(self.tree)
    
    def _countNodes(self, node: Node):

        count = 0

        if not node:
            return 0
        
        count += 1

        for child in node.childs:
            count += self._countNodes(child)
        
        return count
    
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

        sum_rate = 0

        list_rate = [
            ((2, 1, 2), (1, 3, 1), (2, 1, 2)),
            ((2, 1, 2), (1, 4, 1), (2, 1, 2)),
            ((2, 1, 2), (1, 3, 1), (2, 1, 2))       
        ] # gesamtes Feld sind 46

        for z in range(3):

            for y in range(3):

                for x in range(3):

                    if node.field[z][y][x] == const.EMPTY:
                        sum_rate += list_rate[z][y][x]
        
        if self.countZero(node) == 0:
            return
        
        if sum_rate / self.countZero(node) < 2:

            if node.player == True:
                node.win = +1
            
            else:
                node.win = -1

        elif 2 < sum_rate / self.countZero(node) < 1.5:
            node.win = 0

        elif sum_rate / self.countZero(node) < 1.5:

            if node.player == True:
                node.win = -1
            
            else:
                node.win = +1
    
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
    

tree = Tree()

"""""""""
# -1 x
# +1 o
nana.field = [[[0, 0, 0],
               [-1, 0, 0],
               [+1, +1, -1]],
              [[-1, +1, 0],
               [0, +1, -1],
               [+1, -1, 0]],
              [[0, 0, +1],
               [0, +1 , 0],
               [0, 0, 0]]
              ]
"""""""""
tree.build(4, False)
print(tree.countNodes())

# checkWin, checkDraw, countZero,   - funkt