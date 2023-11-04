# configurações iniciais
import pygame
import random


pygame.init()

pygame.display.set_caption("Jogo Snake Python")
largura, altura = 600,400

ecra =pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

# cores RGB
preto = (0, 0, 0)
branca = (255,255,255)
vermelha =(232, 9, 46)
verde = (12, 222, 9)
azul=(53, 38, 212)

# parametros da snake

tamanho_quadrado = 10
velocidade_jogo = 15


def gerar_comida():
    comida_x = round(random.randrange(0,largura-tamanho_quadrado)/ float(tamanho_quadrado))* float(tamanho_quadrado)
    comida_y= round(random.randrange(0,altura-tamanho_quadrado)/ float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(ecra, branca, [pixel[0], pixel[1], tamanho, tamanho])
def desenhar_comida(tamanho,comida_x, comida_y):
    pygame.draw.rect(ecra,verde,[comida_x,comida_y, tamanho,tamanho])


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, azul) # True nao fica pixela, false fica pixala ,
    ecra.blit(texto,[1,1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y =- tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x =- tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y
def rodar_jogo():
    fim_do_jogo = False

    x = largura/2
    y = altura/2

    # snake começa parada, x e y  a 0
    velocidade_x = 0
    velocidade_y = 0

    tamanho_snake= 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_do_jogo:
        ecra.fill(preto)
        # pygame.draw.line(ecra,vermelha,(5,400), (5,5))



        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                fim_do_jogo = True
            elif evento.type==pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        if x < 0 or x >= largura or y <0 or y >= altura:
            fim_do_jogo = True

        #desenhar cominha
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        # atualizar a posição da cobra
        x += velocidade_x
        y += velocidade_y

        # desenhar cobra
        pixels.append([x,y])
        if len(pixels) > tamanho_snake:
            del pixels[0]
        # tirar a cabeça da
        for pixel in pixels[:-1]: # menos o ultimo item para o pixel adicionado nao estar sempre a bater no corpo
            if pixel == [x,y]: # verifica se a cabeça da cobra bateu em alguma parte do corpo
                fim_do_jogo = True

        desenhar_cobra(tamanho_quadrado,pixels)
        desenhar_pontuacao(tamanho_snake-1)


        pygame.display.update()

        # criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_snake +=1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

# criar um loop infinito (jogo a rodar)

# desenhar objetos do jogo no ecra
# pontuação, cobra e comida

# criar logica de terminar o jogo
# o que acontece: cobra bateu na parede ou na propria cobra

# obter a interações do usuario
# fechou a appl
# cliclou as teclas do teclado para mover a cobra




rodar_jogo()