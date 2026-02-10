# Exercícios

## Objetivos

 1. A.
 2. B.
 3. A.
 4. A.
 5. C.
 6. E.
 7. B.
 8. A.
 9. C.
 10. C.
 11. B.
 12. C.
 13. C.
 14. A.
 15. C, pois os dois pixels da grossura, somados nos dois cantos, dá 1 pixel 
    a mais.
 16. C.

## Dissertativas

 1. As coordenadas do sistema do computador possuem as ordenadas invertidas 
    e é decorrente do uso histórico de caracteres para desenhar gráficos, 
    uma fez que são limitados a linhas e letras. Enquanto isso, o sistema 
    de coordenadas cartesiano advém do filosofo e matemático René Descartes.

 2. A importação da biblioteca Pygame e a inicialização de seus módulos através 
    do comando "pygame.init()".

 3. Está no modelo RGB - red, green, blue (vermelho, verde, azul) -, que é 
    uma maneira de representar cores através de combinação.

 4. Quando uma cor não mudará, utilizamos variáveis com nomes totalmente em 
    maiúsculo, o que indica uma constante. Para variáveis de cores que mudam, 
    utiliza-se nomes em minúsculo.

 5. A função "pygame.display.set_mode()" configura a janela, principalmente 
    seu tamanho inicial na tela. Além disso, inicia a própria janela e retorna 
    sua superfície (objeto personalizado do Pygame).

 6. Lida com os eventos da janela do Pygame, como cliques do mouse ou para 
    fechar a janela.

 7. É utilizado para controlar o ciclo de atualização de uma janela Pygame, 
    isto é, pode limitar os quadros por segundo (FPS, frames per second).

 8. "screen" é a superfície da janela principal. É a coordenada primária.
    É a coordenada final. Significa a grossura da linha a ser desenhada.

 9. Criando um laço de repetição com variáveis que mudam a partir de um 
    certo padrão.

 10. O retângulo se torna totalmente preenchido por sua cor.

 11. 20 e 20. Não, o canto superior esquerdo do círculo. 100 e 250.

 12. O valor do arco em radiano, como pi/2.

 13. Configurar a fonte, definir o texto a partir da fonte e renderizar o 
    texto em uma superfície.

 14. Pois a fonte não precisa ser definida a cada renderização, uma vez que 
    não se altera, assim como algumas cores.

 15. [[50,100],[0,200],[200,200],[100,50]]

 16. Troca o buffer da superfície da janela atual por outro buffer. É uma 
    técnica de buffer duplo para evitar ficar renderizando tudo na janela 
    ao mesmo tempo que processa os dados, o que causa erros de renderização.

 17. Termina todos os módulos do Pygame e fecha a janela.

 18. pygame.draw.circle(screen, BLACK, (100, 100), 5, 1)