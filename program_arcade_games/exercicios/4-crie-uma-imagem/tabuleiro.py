from elemento import Elemento
import pygame as pg

class Tabuleiro(Elemento):
    """ Define o tabuleiro de xadrex com as cores preto e branco. """
    def __init__(self, superficie: pg.Surface) -> None:
        """ Configuração inicial do tabuleiro. """
        print("[Tabuleiro - INFO] Configurando tabuleiro.")
        super().__init__(superficie)
        self.width = self.superficie.get_width()
        self.height = self.superficie.get_height()
        self.tile_size = int(600/8)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
    
    def render(self) -> None:
        """ Renderiza a superfície em branco e adiciona os quadrados pretos. """
        self.superficie.fill(self.WHITE)
        
        # Pela matemática, os quadrados pintados de preto serão os que:
        # 1. Estiverem em coordenadas x pares e y ímpares
        # 2. Estiverem em coordenadas x ímpares e y pares
        # Coordenadas em que x e y são ambos pares ou ímpares não terão 
        # quadrados pretos.
        # Além disso, a variável isEven evita recalcular para cada quadrado, 
        # mas o faz para cada fileira, o que diminui o processamento.
        for x in range(0, self.width, self.tile_size):
            isEven = (x/self.tile_size)%2 == 0
            for y in range(0, self.height, self.tile_size):
                if isEven and (y/self.tile_size)%2 == 1 \
                    or not isEven and (y/self.tile_size)%2 == 0:
                    pg.draw.rect(
                        self.superficie,
                        self.BLACK,
                        (x, y, self.tile_size, self.tile_size)
                    )
