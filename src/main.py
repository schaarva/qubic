"""
Qubic
~~~~~

Author: 
Description: Entrypoint
"""

import game

import error 

if __name__ == "__main__":
    try: 
        game.Game().run()
    
    except Exception as err: 
        error.Error.show(err)