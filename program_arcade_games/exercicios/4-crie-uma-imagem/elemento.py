import pygame as pg

class Elemento:
    def __init__(self, superficie: pg.Surface) -> None:
        self.superficie = superficie

    def render(self) -> None:
        pass