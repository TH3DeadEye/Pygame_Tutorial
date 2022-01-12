import pygame ,sys ,os

pygame.init()
#variables
screen_width = 800
screen_height = 600
fps = 60
forse = 5
Player_x = 100
Player_y = 400


clock = pygame.time.Clock()
test_font = pygame.font.Font('./data/Fonts/Pixeltype.ttf',50)
sky_surface = pygame.transform.scale(pygame.image.load(("./data/tilesetOpenGameBackground.png")), (screen_width, 500))

player_surface = pygame.image.load("./data/player/1-Idle/1.png")

player_rect = player_surface.get_rect(midleft = (100,475))

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

    #for movements:
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:#left
        Player_x -= forse
        if Player_x < 0:
            Player_x = 0
    if key[pygame.K_d]:#right
        Player_x += forse
        if Player_x > screen_width - player_surface.get_width():
            Player_x = screen_width - player_surface.get_width()
    if key[pygame.K_w]:#jump
        Player_y -= forse
    if key[pygame.K_s]:#down
        Player_y += forse

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,500))
    screen.blit(player_surface, player_rect)
    screen.blit(text_surface, (350,50))


    pygame.display.update()
    clock.tick(fps)
