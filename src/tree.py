"""
Qubic
~~~~~

Author: Timo
Description: Game tree
"""
import copy
import random

import const


LIST_WIN = [                         # (z, y, x)
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


class Node:
    """
    A node class for game tree.
    
    Field:
    ~~~~~
                   z
              / 2
         / 1
        0------1------2 x
        |
        |
        1
        |
        |
        2
        y
    """
    
    def __init__(self):

        self.field = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ] # BUG
        self.childs = []
        self.win = 0
        self.player = True
        self.change = None
        self.over = False

        # Special cases
        
        self.rate_win = False
        self.rate_block = False

class Tree:
    """A game tree class."""
    
    def __init__(self):
        """Initializes a new tree."""

        self.tree = Node()
        self.tree.player = True # Ist jetzt (im nächsten Zug) der Player dran?

        self.build()

    def build(self) -> None:
        """Extend tree structure."""
      
        self._build(self.tree, 2)
            # 1 (akku save)
            # 2 (normal)
            # 3 (intelligent)
            # 4 (wait a few sec)
            # 5 (data center)
            # ...
            # 20 (unplayable)

    def _build(self, node: Node, max_height: int) -> None:
        """
        Extend the tree structure.
        
        node: A Node object.
        max_height: The maximum depth of tree.
        """
        
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
                        new_child.player = not node.player

                        if new_child.player:
                            new_child.field[y][x][z] = const.CIRCLE 

                        else:
                            new_child.field[y][x][z] = const.CROSS

                        # Check for duplicates

                        for child in node.childs:
                            if child.change == new_child.change: # Do with old one
                                self._build(child, max_height-1)
                        
                        else: # Do with new one
                            
                            node.childs += [new_child]
                            self._build(new_child, max_height-1)
    
    def rateNegamax(self) -> None:
        """Rate tree by negamax."""

        self.rateNegamax_(self.tree)

    def rateNegamax_(self, node: Node) -> int:
        """
        Rate tree by negamax.
        
        node: A Node object.
        """
       
        # Someone won

        if self.checkWin(node):
            
            node.over = True
            node.rate_win = True
            
            if node.player:
                node.win = -1
            
            else:
                node.win = +1
            
            return node.win
        
        # Field full
        
        if self.countZero(node) == 0:

            node.over = True
            
            node.win = 0
            return node.win
            
        # End of tree

        if not node.childs:
                
            node.win = self.rateCustom(node)
            return node.win

        maxi = -1
        
        for child in node.childs:

            win = -self.rateNegamax_(child)

            if win > maxi:
                maxi = win

        node.win = maxi

        return maxi

    def rateCustom(self, node: Node) -> int:
        """
        Rate by custom rating.
        
        node: A node object.
        """

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

            if node.player:
                return -1
            
            else:
                return +1

        elif 2 >= sum_rate / self.countZero(node) > 1.5:
            return 0

        elif 1.5 >= sum_rate / self.countZero(node):

            if node.player:
                return +1
            
            else:
                return -1
    
    def checkBlock(self) -> None:
        """Check a position for an enemy block."""

        self._checkBlock(self.tree)
        
    def _checkBlock(self, node: Node) -> None:
        """
        Check a position for an enemy block.

        node: A node object.
        """
        
        if not node:
            return
        
        for child in node.childs:
            
            for win in LIST_WIN:
                for place1, place2, place3 in ((0, 1, 2), (1, 2, 0), (0, 2, 1)):

                    if (node.field[win[place1][0]][win[place1][1]][win[place1][2]]
                        == node.field[win[place2][0]][win[place2][1]][win[place2][2]]
                        == const.CROSS):
                        
                        if node.field[win[place3][0]][win[place3][1]][win[place3][2]] == const.CIRCLE:
                            node.rate_block = True
            
            self._checkBlock(child)

    def checkWin(self, node: Node) -> bool:
        """
        Check a pos for a win.
        
        node: A node object.
        """
    
        for win in LIST_WIN:

            if (node.field[win[0][0]][win[0][1]][win[0][2]]
                == node.field[win[1][0]][win[1][1]][win[1][2]]
                == node.field[win[2][0]][win[2][1]][win[2][2]]):

                if node.field[win[0][0]][win[0][1]][win[0][2]] != const.EMPTY:
                    return True
                    
        return False

    def countZero(self, node: Node) -> int:
        """
        Count the number of empty fields.

        node: A node object.
        """

        zero = 0

        for x in range(3):
            
            for y in range(3):
                
                for z in range(3):

                    if node.field[x][y][z] == 0:
                        zero += 1

        return zero

    # In-Game functions
    
    def ai_input(self) -> None:
        """An AI makes a move."""
        
        if not self.tree.childs:
            return
        
        childs = self.tree.childs

        win_win = []     # Gewonnen
        draft_block = [] # Blocken
        win = []         # Wahrscheinlich gewonnen
        draft = []       # Unentschieden
        loose = []       # Verloren

        for child in childs:
            
            if child.rate_win:  
                win_win += [child]
        
            elif child.rate_block:
                draft_block += [child]
        
            elif child.win == -1:
                win += [child]

            elif child.win == 0:
                draft += [child]

            else:
                loose += [child]

        random.shuffle(win_win)
        random.shuffle(draft_block)
        random.shuffle(win)
        random.shuffle(draft)
        random.shuffle(loose)

        childs = win_win + draft_block + win + draft + loose
        
        self.tree = childs[0]

        self.build()
        self.rateNegamax()
    
    def player_input(self, cor: tuple) -> None:
        """
        The player makes a move.
        
        cor: A tuple of (z, y, x) coordinates.
        """
        
        for child in self.tree.childs:

            child: Node

            if child.change == cor:
                
                self.tree = child

                self.build()
                self.rateNegamax()
                self.checkBlock()
    
    # Debug functions

    def printNodes(self) -> None:
        """Print the tree structure."""


        self._printNodes(self.tree, 0)
    
    def _printNodes(self, node: Node, __height) -> None:
        """
        Print the tree structure.

        node: A node object.
        """

        if not node:
            return
        
        print(__height * "  ", node.player)

        for child in node.childs:
            self._printNodes(child, __height + 1)

    def countNodes(self) -> int:
        """Count the number of nodes."""

        return self._countNodes(self.tree)
    
    def _countNodes(self, node: Node) -> int:
        """
        Count the number of nodes.
        
        node: A node object.
        """

        if not node:
            return 0

        count = 1

        for child in node.childs:
            count += self._countNodes(child)

        return count
    
    def printField(self, node: Node) -> None:
        """
        Print information about a node.
        
        node: A node object.
        """

        print("Win:", node.win, "Player:", node.player, "Over:", node.over)
        print(node.field[0][0], "\t", node.field[1][0], "\t", node.field[2][0])
        print(node.field[0][1], "\t", node.field[1][1], "\t", node.field[2][1])
        print(node.field[0][2], "\t", node.field[1][2], "\t", node.field[2][2])
    
    def printFields(self, node: Node) -> None:
        """
        Print information about the childs of a node.
        
        node: A node object.
        """

        for child in node.childs:
            
            self.printField(child)
            print()

    def printChanges(self, node: Node) -> None:
        """
        Print the next moves of a node.
        
        node: A node object.
        """

        for child in node.childs:

            child: Node

            print(child.change)


if __name__ == "__main__":

    tree = Tree()
    node = Node()
    node.field = [
        [[1, 0, -1], [0, -1, 0], [-1, -1, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]],
        [[0, 0, 0], [1, 0, 0], [0, 0, 1]]
    ]
    
    print(tree.checkWin(node))
    # tree.printChanges(tree.tree)
    # print(len([child.change for child in tree.tree.childs]))
    # tree.printFields(tree.tree)

    # checkWin, checkDraw, countZero,   - funkt