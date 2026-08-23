#Surfaces: Images, imported png and text
#          - can also serve as a window (display surface)
#Rectangles: wraps around a surface and positions it, also does collision
#Updates: Literally just a for loop, on every iteration we get input, update elements and draw a frame

# Display surfaces: The canvas that everything will be drawn on, you can only have one at a time.
# Event Loop: Checks (keyboards, mouse & controller input, timers) This also includes pressing x to close the game
# Pygame can display graphics in 2 ways: Show an image or text via a surface and draw pixels. 
# A surface in Pygame is usually an image (png, jpg) a plain area or rendered text. 
# How to create a surface plain surface: pygame.surface((width, height))
# How to create an imported surface: pygame.image.load(path)
# How to create a text surface: font.render(text, AntiAlias, Color)


import pygame


# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')  #sets the caption for window
running = True

# surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# import an image
player_surf = pygame.image.load('space game/images/player.png')


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    # draw the game
    display_surface.fill('darkgray')
    x += 0.1
    display_surface.blit(player_surf, (x, 150))   #one surface on another surface
    pygame.display.update()




pygame.quit() # closes the game