"""
Qubic
~~~~~

Author: 
Description: Game tree
"""

class Node:
    """A node class for game tree."""
    
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
    
    def negamax(self, node: Node):
        """Rate by negamax."""

        ...
    
    def rate(self, node: Node):
        """Rate by custom rating."""

        ...
    
    def checkWin(self):
        """Check a pos for a win."""

        ...
    
    def checkDraw(self):
        """Check a pos for a draw."""

        ...