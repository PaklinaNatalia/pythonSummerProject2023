import pygame, os

pygame.init()

#Всякие переменные
screen_width = 1200 #Ширина экрана
screen_height = 750 #Высота экрана
item_size = 128 #Размер скрытого предмета
board_width = 5 #Ширина доски
board_height = 5 #Высота доски
tile_padding = 10 #Расстояние между плитками
lr_margin = (screen_width - ((item_size + tile_padding) * board_height)) // 2 #Расчет расстояния до краев лево-право
tb_margin = (screen_height - ((item_size + tile_padding) * board_width)) // 2 #Расчет расстояния до краев верх-низ
WHITE = (255, 255, 255) #Цвет оборота карточки
select_1 = None #Выбрана 1ая плитка
select_2 = None #Выбрана 2ая плитка
game_score = 0 #Счет
game_turns = 0 #Число ходов

#Экран
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_icon = pygame.image.load("ui/galaxy.png")
pygame.display.set_icon(game_icon)
bg_image = pygame.image.load("ui/universe.jpg")
bg_image_rect = bg_image.get_rect()

running = True
while running:
    game_screen.blit(bg_image, bg_image_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()