import pygame as pg
from math import pi as PI
import sys

def main() -> None:
    # Inicia os módulos do Pygame
    pg.init()
    
    # Cores em RGB
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
    size = (700, 500)
    screen = pg.display.set_mode(size)
    
    pg.display.set_caption("Joguinho!")
    
    # Controla o relógio da janela, isto é,
    # a atualização do programa.
    clock = pg.time.Clock()
    
    font = pg.font.SysFont("Arial", 15, True, False)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        text = font.render("FPS: " + str(int(clock.get_fps())), True, BLACK)
        
        screen.fill(WHITE)
        
        pg.draw.line(screen, BLACK, (0, 0), (100, 100), 2)
        pg.draw.rect(screen, BLACK, (100, 100, 100, 100), 0)
        pg.draw.ellipse(screen, BLACK, (100, 100, 100, 100), 2)
        pg.draw.polygon(screen, BLACK, ((200, 200), (250, 200), (225, 225)), 2)
        
        screen.blit(text, (screen.get_width() - text.get_width(), 0))

        pg.display.flip()

        # Limita as atualizações, isto é, o FPS
        # para 60 fps.
        # clock.tick(60)
        clock.tick(60)


if __name__ == "__main__":
    main()