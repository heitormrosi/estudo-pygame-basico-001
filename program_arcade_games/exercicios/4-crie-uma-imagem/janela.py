import pygame as pg
import sys

from elemento import Elemento

class Janela:
    """ Janela pricipal. """
    def __init__(self, titulo: str, tamanho: tuple[int, int]) -> None:
        """ Configuração inicial da janela. """
        print("[Janela - INFO] Configurando janela principal.")
        # Configuração padrão para janela Pygame
        self.screen = pg.display.set_mode(tamanho)
        pg.display.set_caption(titulo)
        
        # Controla o ciclo de renderização, isto é, os quadros por segundo
        self.clock = pg.time.Clock()
        self.fps = 60
        
        # Incluir padrão de laço de eventos
        self.elementos = []
    
    def get_surface(self) -> pg.Surface:
        """ Retorna a superfície da janela. """
        return self.screen
    
    def add_element(self, elemento: Elemento) -> None:
        """ Adiciona um elemento à lista de elementos para renderização. """
        self.elementos.append(elemento)
    
    def render(self) -> None:
        """ 
            Requisita a todos os elementos na lista de renderização para que
        se renderizem. 
        """
        for elemento in self.elementos:
            elemento.render()
    
    def run(self) -> None:
        """ Executa o laço de repetição principal do programa. """
        print("[Janela - INFO] Executando janela principal.")
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            self.render()

            # Troca os dois buffers de renderização de lugar.
            # O que estava renderizando se esconde e o que estava escondido
            # começa a ser renderizado.
            pg.display.flip()
            self.clock.tick(self.fps)