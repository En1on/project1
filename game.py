import pygame
import random
import time

pygame.init()

gameScreen = pygame.display.set_mode((400, 300))

FPS = pygame.time.Clock()
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Игра года")
gameScreen.fill((100,220,255))
# pygame.display.flip()

win_wall_img = "wall_banner_red.png"
wall_img = 'wall_column_mid.png'
wall = pygame.image.load(wall_img)
win_wall = pygame.image.load(win_wall_img)

player_r_go = [
    "player_1.png",
    "player_2.png",
    "player_3.png",
    "player_4.png",
    "player_5.png",
    "player_6.png",
    "player_7.png",
    "player_8.png",
]

player_l_go = [
    "player_1_l.png",
    "player_2_l.png",
    "player_3_l.png",
    "player_4_l.png",
    "player_5_l.png",
    "player_6_l.png",
    "player_7_l.png",
    "player_8_l.png",
]
count = 0
direcrtion = "right"
r_player = 0
l_player = 0
dir_player = []
image_player, player_direction = None, None
dir_player_costum = None

walls_coordinates = []
walls_coordinates_win = []

def get_player(img_name, player_direction, dir_player_costum):
    global image_player, player , direcrtion
    if direcrtion != player_direction:
        direcrtion = player_direction
        dir_player = dir_player_costum
    image_player = pygame.image.load(img_name)
    player = image_player.get_rect()

get_player(player_r_go[count] ,'right',player_r_go)

place_x, place_y = 150, 150

pygame.draw.rect(screen, (255,0,0), player)
screen.blit(image_player, (place_x, place_y))

def add_coordinates(x = None, y = None):
    global walls_coordinates
    for i in range(4):
        walls_coordinates.append([x+i*5 , y+i*5])

def add_coordinates_win(x = None , y = None):
    global walls_coordinates_win
    for i in range(4):
        walls_coordinates_win.append([x+i*5,y+i*5])

def draw_wall():
    horisontal_wall = pygame.transform.rotate(wall, 90)

    for i in range(27):
        screen.blit(wall, (10, 50+i*15))
        add_coordinates(10, 50+i*15)
        if i == 26:
            for j in range(27):
                screen.blit(horisontal_wall, (10+j*15, 50+i*15))
                add_coordinates(10+j*15, 50+i*15)

    for i in range(27):
        screen.blit(horisontal_wall, (10+i*15, 50))
        add_coordinates(10+i*15, 50)
        if i == 13:
            for j in range(25):
                screen.blit(wall, (10+i*15, 50+j*15))
                add_coordinates(10+i*15, 50+j*15)
        elif i == 26:
            for j in range(27):
                screen.blit(wall, (10+i*15, 50+j*15))
                add_coordinates(10+i*15, 50+j*15)
        

def darw_win_wall():
    screen.blit(win_wall, (300 , 300))
    add_coordinates_win(300,300)


runGame = True 
while runGame:
    gameScreen.fill((100,220,255))
    draw_wall()
    darw_win_wall()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: runGame = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if count != 7:
                count += 1
            else:
                count = 0
            get_player(player_r_go[count] ,'',player_r_go)
            place_y -=5
        if event.key == pygame.K_DOWN:
            if count != 7:
                count += 1
            else:
                count = 0
            get_player(player_r_go[count] ,'',player_r_go)
            place_y +=5
        if event.key == pygame.K_LEFT:
            if count != 7:
                count += 1
            else:
                count = 0
            get_player(player_l_go[count] ,'left',player_l_go)
            place_x -=5
        if event.key == pygame.K_RIGHT:
            if count != 7:
                count += 1
            else:
                count = 0
            get_player(player_r_go[count] ,'right',player_r_go)
            place_x +=5

    if [place_x, place_y] in walls_coordinates_win:
        print("you win")
        runGame = False           

    if [place_x, place_y] in walls_coordinates:
        place_x,place_y = 150,150
    
    pygame.draw.rect(screen, (255,0,0), player)
    screen.blit(image_player, (place_x, place_y))
    
    pygame.display.update()
    FPS.tick(30)
time.sleep(2)
pygame.quit()
