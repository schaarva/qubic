"""
Qubic
~~~~~

Author: 
Description: Game tree
"""
import copy

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
        self.change = None

class Tree:
    """A game tree class."""
    
    def __init__(self):

        self.tree = Node()
        self.tree.player = False

        self.build()

    def build(self):
        """Extend tree structure."""
      
        self._build(self.tree, 1)

    def _build(self, node: Node, max_height: int):
        
        if max_height == 0:
            return
        
        for y in range(3):

            for x in range(3):

                for z in range(3):
                    
                    if node.field[y][x][z] == const.EMPTY:

                        # Create new node
                        
                        new_child = Node()
                        new_child.change = (y, x, z)
                        new_child.field = copy.deepcopy(node.field)

                        if new_child.player:
                            new_child.field[y][x][z] = const.CROSS 

                        else:
                            new_child.field[y][x][z] = const.CIRCLE
                        
                        new_child.player = not node.player

                        # Check for duplicates

                        created = []

                        for child in node.childs:
                            created += [child.change]

                        if (y, x, z) in created:
                            continue

                        node.childs += [new_child]

                        self._build(new_child, max_height-1)
    
    def printNodes(self):
        self._printNodes(self.tree, 0)
    
    def _printNodes(self, node: Node, __height):

        if not node:
            return
        
        print(__height * "  ", "o")

        for child in node.childs:
            self._printNodes(child, __height + 1)

    def countNodes(self):
        return self._countNodes(self.tree)
    
    def _countNodes(self, node: Node):

        if not node:
            return 0

        count = 1

        for child in node.childs:
            count += self._countNodes(child)

        return count        
    
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
                node.win = self.rateCustom(node)
            
            return node.win

        maxi = -1
        
        for child in node.childs:

            win = -self.rateNegamax_(child)

            if win > maxi:
                maxi = win

        node.win = maxi

        return maxi
    
    def printField(self, node: Node):

        print(node.field[0][0], "\t", node.field[1][0], "\t", node.field[2][0])
        print(node.field[0][1], "\t", node.field[1][1], "\t", node.field[2][1])
        print(node.field[0][2], "\t", node.field[1][2], "\t", node.field[2][2])
    
    def printChanges(self, node: Node):

        for child in node.childs:

            child: Node

            print(child.change)
    
    def printFields(self, node: Node):

        for child in node.childs:

            child: Node

            print(child.field[0][0], "\t", child.field[1][0], "\t", child.field[2][0])
            print(child.field[0][1], "\t", child.field[1][1], "\t", child.field[2][1])
            print(child.field[0][2], "\t", child.field[1][2], "\t", child.field[2][2])
            print()

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
        
        if 4 > sum_rate / self.countZero(node) > 2:

            if node.player == True:
                return +1
            
            else:
                return -1

        elif 2 > sum_rate / self.countZero(node) > 1.5:
            return 0

        elif 1.5 > sum_rate / self.countZero(node):

            if node.player == True:
                return -1
            
            else:
                return +1

    def checkWin(self, node: Node):
        """Check a pos for a win."""
        
        list_win = [                         # (z, y, x)
            ((0, 0, 0), (0, 0, 1), (0, 0, 2)), # Layer 0 von vorn
            ((0, 1, 0), (0, 1, 1), (0, 1, 2)),
            ((0, 2, 0), (0, 2, 1), (0, 2, 2)),
            ((0, 0, 0), (0, 1, 0), (0, 2, 0)),
            ((0, 0, 1), (0, 1, 1), (0, 2, 1)),
            ((0, 0, 2), (0, 1, 2), (0, 2, 2)),
            ((0, 0, 0), (0, 1, 1), (0, 2, 2)),
            ((0, 0, 2), (0, 1, 1), (0, 2, 0)),
            
            ((1, 0, 0), (1, 0, 1), (1, 0, 2)), # Layer 1 von vorn
            ((1, 1, 0), (1, 1, 1), (1, 1, 2)),
            ((1, 2, 0), (1, 2, 1), (1, 2, 2)),
            ((1, 0, 0), (1, 1, 0), (1, 2, 0)),
            ((1, 0, 1), (1, 1, 1), (1, 2, 1)),
            ((1, 0, 2), (1, 1, 2), (1, 2, 2)),
            ((1, 0, 0), (1, 1, 1), (1, 2, 2)),
            ((1, 0, 2), (1, 1, 1), (1, 2, 0)),
            
            ((2, 0, 0), (2, 0, 1), (2, 0, 2)), # Layer 2 von vorn
            ((2, 1, 0), (2, 1, 1), (2, 1, 2)),
            ((2, 2, 0), (2, 2, 1), (2, 2, 2)),
            ((2, 0, 0), (2, 1, 0), (2, 2, 0)),
            ((2, 0, 1), (2, 1, 1), (2, 2, 1)),
            ((2, 0, 2), (2, 1, 2), (2, 2, 2)),
            ((2, 0, 0), (2, 1, 1), (2, 2, 2)),
            ((2, 0, 2), (2, 1, 1), (2, 2, 0)),
            
            ((0, 0, 0), (1, 0, 0), (2, 0, 0)), # Layerübergreifend längs
            ((0, 0, 1), (1, 0, 1), (2, 0, 1)),
            ((0, 0, 2), (1, 0, 2), (2, 0, 2)),
            ((0, 1, 0), (1, 1, 0), (2, 1, 0)),
            ((0, 1, 1), (1, 1, 1), (2, 1, 1)),
            ((0, 1, 2), (1, 1, 2), (2, 1, 2)),
            ((0, 2, 0), (1, 2, 0), (2, 2, 0)),
            ((0, 2, 1), (1, 2, 1), (2, 2, 1)),
            ((0, 2, 2), (1, 2, 2), (2, 2, 2)),

        
            ((0, 0, 0), (1, 1, 1), (2, 2, 2)), # Raumdiagonalen
            ((2, 0, 0), (1, 1, 1), (0, 2, 2)),
            ((2, 0, 2), (1, 1, 1), (0, 2, 0)),
            ((0, 0, 2), (1, 1, 1), (2, 2, 0)),
            ((0, 0, 0), (1, 1, 0), (2, 2, 0)),
            ((0, 0, 1), (1, 1, 1), (2, 2, 1)),
            ((0, 0, 2), (1, 1, 2), (2, 2, 2)),
            ((0, 2, 0), (1, 1, 0), (2, 0, 0)),
            ((0, 2, 1), (1, 1, 1), (2, 0, 1)),
            ((0, 2, 2), (1, 1, 2), (2, 0, 2)),
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

    def countZero(self, node: Node):

        zero = 0

        for x in range(3):
            
            for y in range(3):
                
                for z in range(3):

                    if node.field[x][y][z] == 0:
                        zero += 1

        return zero
    
    def ai_input(self):
        
        if not self.tree.childs:
            return
        
        childs = self.tree.childs
        childs.sort(key = lambda node: node.win)
        
        self.tree = childs[0]

        self.build()
        self.rateNegamax()
    
    def player_input(self, cor: tuple):
        
        for child in self.tree.childs:

            child: Node

            if child.change == cor:
                
                self.tree = child

                self.build()
                self.rateNegamax()

if __name__ == "__main__":

    tree = Tree()
    
    tree.build()
    tree.rateNegamax()
    tree.printNodes()
    # tree.printChanges(tree.tree)
    # print(len([child.change for child in tree.tree.childs]))
    # tree.printFields(tree.tree)

    # checkWin, checkDraw, countZero,   - funkt