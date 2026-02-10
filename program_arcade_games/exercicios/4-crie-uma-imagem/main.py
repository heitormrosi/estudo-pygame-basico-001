"""
Situação e trabalho: criar uma imagem com os gráficos do Pygame.

Ação: vou criar um tabuleiro de xadrez e algumas peças.

Resultado: um tabuleiro de xadrex com as peças em ordem e começando com 
    as brancas em baixo.
"""

from janela import Janela
from tabuleiro import Tabuleiro

def main() -> None:
    TITULO = "Imagem de tabuleiro de xadrex com Python e Pygame"
    TAMANHO = (600, 600)
    
    janela = Janela(TITULO, TAMANHO)
    tabuleiro = Tabuleiro(janela.get_surface())
    
    janela.add_element(tabuleiro)
    
    janela.run()


if __name__ == "__main__":
    main()