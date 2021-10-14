from hashlib import new
import pygame, random, sys
from pygame.locals import *
import pygame.freetype
import time 

def inicia():
    """Inicia"""
    pygame.init()
    screen = pygame.display.set_mode((600, 630))
    pygame.display.set_caption('Sny-Snake-RGB')

    """Variaveis"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    pontos = 0
    tick = 15
    space = False
    timer = 0.01

    """Define o grid e corrige a numeração divide o numero para inteiro e multiplica"""
    def on_grid_random():
        x = random.randint(10,570)
        y = random.randint(10,570)
        return (x//10 * 10 , y//10 * 10)
    """Colisão com a maça"""
    def collision(c1,c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1])
    """Colisão com a tela"""
    def collider(c3, c4):
        return (c3[0] == 590) or (c3[0] == 0) or (c4[1] == 590) or (c4[1] == 0)
    """Troca a cor da cobra"""
    def newColorSnake():
        x = random.randint(0,255)
        y = random.randint(0,255)
        z = random.randint(0,255)
        return (x,y,z)
    """Cria pontuação"""
    def pontuacao():
        pygame.font.init()
        jogoFonte = pygame.font.Font('./Gratise.ttf',25)
        text = jogoFonte.render('Pontos: ' + str(pontos),True,(255,255,255))
        textRect = text.get_rect()
        textRect.center = (300,615)
        screen.blit(text,textRect)
        nivel = ""

        if space == False:
            textInicial = jogoFonte.render('Espaço para iniciar',True,(255,255,255))
            textInicialRect = text.get_rect()
            textInicialRect .center = (230,200)
            screen.blit(textInicial,textInicialRect )


            nivel = jogoFonte.render('NORMAL',True,(255,255,255))
            textRect = text.get_rect()
            textRect.center = (300,330)
            screen.blit(nivel,textRect)

            strtick = jogoFonte.render('TICK:   ' + str(tick),True,(255,255,255))
            strRect = strtick.get_rect()
            strRect.center = (280,380)
            screen.blit(strtick,strRect)


        if pontos == 5:
            nivel = jogoFonte.render('FÁCIL',True,(255,255,255))
            textRect = text.get_rect()
            textRect.center = (300,315)
            screen.blit(nivel,textRect)
            nivel = jogoFonte.render('',True,(255,255,255))
            screen.blit(nivel,textRect)

            strtick = jogoFonte.render('TICK:   ' + str(tick),True,(255,255,255))
            strRect = strtick.get_rect()
            strRect.center = (280,380)
            screen.blit(strtick,strRect)
            strtick = jogoFonte.render('',True,(255,255,255))
            screen.blit(strtick,strRect)

        if pontos == 10:
            nivel = jogoFonte.render('MÉDIO',True,(255,255,255))
            textRect = text.get_rect()
            textRect.center = (300,315)
            screen.blit(nivel,textRect)
            nivel = jogoFonte.render('',True,(255,255,255))
            screen.blit(nivel,textRect)

            strtick = jogoFonte.render('TICK:  ' + str(tick),True,(255,255,255))
            strRect = strtick.get_rect()
            strRect.center = (280,380)
            screen.blit(strtick,strRect)
            strtick = jogoFonte.render('',True,(255,255,255))
            screen.blit(strtick,strRect)

        if pontos == 20:
            nivel = jogoFonte.render('DIFÍCIL',True,(255,255,255))
            textRect = text.get_rect()
            textRect.center = (300,315)
            screen.blit(nivel,textRect)
            nivel = jogoFonte.render('',True,(255,255,255))
            screen.blit(nivel,textRect)

            strtick = jogoFonte.render('TICK:   ' + str(tick),True,(255,255,255))
            strRect = strtick.get_rect()
            strRect.center = (280,380)
            screen.blit(strtick,strRect)
            strtick = jogoFonte.render('',True,(255,255,255))
            screen.blit(strtick,strRect)

    
    """Grid RBG"""
    def grid():
        x = 0
        y = 590
        while x < 590:
            x = x+1
            grid1 = [(y,x),(x,y)]
            grid2 = [(x,y),(x,y)]
            grid3 = [(0,x),(y,x)]
            grid4 = [(x,0),(y,x)]

            grid_skin = pygame.Surface((10,10)) 
            grid_skin.fill(newColorSnake())
            screen.blit(grid_skin, grid1)
            screen.blit(grid_skin, grid2)
            screen.blit(grid_skin, grid3)
            screen.blit(grid_skin, grid4)
    
    """---------------"""
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill(newColorSnake())


    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill((255, 0, 0))

    my_direction = 5

    clock = pygame.time.Clock()

    """CONFIG JOGOS"""

    while True:
        clock.tick(tick)

        """Detecta Movimento"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if space == False:
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        space = True
                        my_direction: UP

            if space == True:
                if event.type == KEYDOWN:
                    if event.key == K_UP and my_direction != DOWN:
                            my_direction = UP
                    if event.key == K_DOWN and my_direction != UP:
                            my_direction = DOWN
                    if event.key == K_LEFT and my_direction != RIGHT:
                            my_direction = LEFT
                    if event.key == K_RIGHT and my_direction != LEFT:
                            my_direction = RIGHT

        """Colisão com a maça"""
        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0,0))
            snake_skin.fill(newColorSnake())
            pontos = pontos + 1
        
        """Colisão com a tela"""
        if collider(snake[0],snake[1]):
            event.type = QUIT
            pygame.quit
            
        """Faz o movimento"""
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = snake[i-1][0], snake[i-1][1]

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
            
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
            
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
            
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])


        screen.fill((0, 0, 0))
        screen.blit(apple, apple_pos)
        pontuacao()
    
        if pontos >= 2:
            tick = 18
            pontuacao()

        if pontos >= 5:
            tick = 20
        
        if pontos >= 10:
            tick = 22
        
        if pontos >= 15:
            tick = 30

        if space != False:
            for pos in snake:
                screen.blit(snake_skin, pos)

        grid()

        pygame.display.update()

if (__name__ == "__main__"):
    inicia()