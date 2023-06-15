"""
Qubic
~~~~~

Author: Arne
Description: Entrypoint
"""

import game
import error



if __name__ == "__main__":
    
    # try:
        
    g = game.Game()
    g.run()
    
    # except Exception as err:
        
    #     try: g.quit()
    #     except: pass

    #     error.Error_().show(err)