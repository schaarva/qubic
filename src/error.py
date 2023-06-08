"""
Qubic
~~~~~

Author: Arne
Description: Error message
"""
import pygame 
import easygui as e

class Error_:
    """A class for an error message window."""

    def show(self, err: Exception):
        """Show the message window."""
        e.msgbox(err, "An error has occured!")
        
        