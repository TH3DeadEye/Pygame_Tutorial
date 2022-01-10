import pygame ,sys ,os

pygame.init()
#variables
screen_width = 800
screen_height = 600
fps = 60

clock = pygame.time.Clock()
test_font = pygame.font.Font('./data/Fonts/Pixeltype.ttf',50)

sky_surface = pygame.transform.scale(pygame.image.load(("./data/tilesetOpenGameBackground.png")), (screen_width, 450))

player_surface = pygame.image.load("./data/player/1-Idle/1.png")
Player_x = 100
Player_y = 400

ground_surface = pygame.image.load("./data/ground.png")

text_surface = test_font.render("My Game", False, "Black")


#the actual screen for our game 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Runner ")

while True: # the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,450))
    Player_x -=1
    screen.blit(player_surface, (Player_x,Player_y))
    screen.blit(text_surface, (350,50))


    pygame.display.update()
    clock.tick(fps)
