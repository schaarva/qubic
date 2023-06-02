"""
Qubic
~~~~~

Author: Valentin
Description: Status bar
"""

import pygame


class Infos:
    """A class for a status bar."""

    def __init__(self):
        
        self.fps = 0
        self.time = [0, 0]

        self.font = pygame.font.SysFont("Arial", 50)
    
    def set_time(self, minutes: int, seconds: int):

        self.time = minutes, seconds

        if minutes > 99:
            self.time[0] = 99
        
        elif seconds > 99:
            self.time[1] = 99
    
    def set_fps(self, fps: int):
        
        self.fps = fps

        if fps > 999:
            self.fps = 999
    
    def render(self):

        bar = pygame.surface.Surface((1280, 720)).convert_alpha()
        bar.fill((0, 0, 0, 0))

        surface_time = self.font.render(
            f"{self.time[0]:02d}:{self.time[1]:02d}", False, (0, 0, 0))
        surface_time = surface_time.convert_alpha()

        surface_fps = self.font.render(
            f"{self.fps} FPS".rjust(3), False, (0, 0, 0))
        surface_fps = surface_fps.convert_alpha()

        return [
            (bar, (0, 0)),
            (surface_time, (105, 40)),
            (surface_fps, (1060, 40))
        ]