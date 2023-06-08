"""
Qubic
~~~~~

Author: Arne
Description: Entrypoint
"""

import game
import error



if __name__ == "__main__":
    
    try: 
        game.Game().run()
        #raise TypeError("lol")
    
    
    except Exception as err: 
        error.Error_().show(err)