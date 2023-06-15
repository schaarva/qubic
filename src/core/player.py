"""
Qubic
~~~~~

Autor: Arne
Description: Player input
"""

import core.tree



def player_input(pos: core.tree.Node, cor: tuple | list) -> core.tree.Node:
    """Player move"""
    
    for child in pos.childs:
        print(child.change, cor)
        if child.change == cor:
            return child