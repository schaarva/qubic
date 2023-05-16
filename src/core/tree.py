"""
Qubic
~~~~~

Author: 
Description: Game tree
"""

class Node:
    """A node class for game tree."""
    
    def __init__(self):

        self.field = []
        self.win = 0

    ...


class Tree:
    """A game tree class."""
    
    def __init__(self):
        self.tree = None
    
    def build(self, max_nodes: int):
        """Extend the tree structure."""

        ...
    
    def evaluate(self):
        """Rate the win pos."""

        # self.negamax() -> end
        # self.rate() -> open

        ...
    
    def rateNegamax(self, node: Node):
        """Rate by negamax."""

        ...
    
    def rateCustom(self, node: Node):
        """Rate by custom rating."""

        ...
    
    def checkWin(self, node: Node):
        """Check a pos for a win."""

        ...
    
    def checkDraw(self, node: Node):
        """Check a pos for a draw."""

        ...