"""
Qubic
~~~~~

Author: Valentin
Description: Start and end screen
"""
import pygame

import const


class State:
    """A class for info screens."""

    def __init__(self):
        """Initializes a new info screen."""

        self.state = 0
        self.win = 0
        
        self.image_welcome = pygame.image.load(
            "./assets/images/welcome.png").convert_alpha()
        self.image_loss = pygame.image.load(
            "./assets/images/loss.png").convert_alpha()
        self.image_win = pygame.image.load(
            "./assets/images/win.png").convert_alpha()
        self.image_draft = pygame.image.load(
            "./assets/images/draft.png").convert_alpha()
    
    def set_state(self, state: int) -> None:
        """
        Set the state of the game.

        state: The game state. (-> const)
        """

        self.state = state

        if not state in (-1, 0, 1):
            self.state = 0
    
    def set_win(self, win: int) -> None:
        """
        Set the current win position.
        
        win: The win position. (w: 1, d: 0, l: -1)
        """

        self.win = win

        if not win in (-1, 0, 1):
            self.win = 0
    
    def render(self) -> list:
        """Render the info screens."""

        surface_state = pygame.surface.Surface((1280, 720)).convert_alpha()
        surface_state.fill((0, 0, 0, 0))

        if self.state == const.STATE_OVER:

            if self.win == -1:
                surface_state = self.image_loss
            
            elif self.win == 0:
                surface_state = self.image_draft
            
            elif self.win == 1:
                surface_state = self.image_win
        
        elif self.state == const.STATE_READY:
            surface_state = self.image_welcome

        return [(surface_state, (0, 0))]