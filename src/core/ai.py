"""
Qubic
~~~~~

Autor: Arne
Description: AI input
"""

import core.tree


def ai_input(self, pos: core.tree.Node) -> core.tree.Node:
    """Get next AI pos."""

    if not childs:
        return None
    
    childs = pos.childs
    childs.sort(key = lambda node: node.win)
    
    return childs[0]