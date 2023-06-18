"""
Qubic
~~~~~

Author: Arne
Description: Error message
""" 
import easygui


class Error_:
    """A class for an error message window."""

    def show(self, err: Exception) -> None:
        """Show the message window."""
        
        easygui.msgbox(err, "An error has occured!")