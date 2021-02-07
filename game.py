import pygame
from util import load_image
from assets.drew import Drew

def main():
    pygame.init()
    screen_flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((0, 0), screen_flags)
    pygame.mouse.set_visible(0)

    background, _ = load_image("main_bg.png")
    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    drew = Drew([200, 500])
    allsprites = pygame.sprite.RenderPlain((drew))
    running = True
    walk_values = [0, 0] # x and y origin is in top left
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                walk_values[1] -= 10

            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                walk_values[0] += 10

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                walk_values[1] += 10

            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                walk_values[0] -= 10


            if event.type == pygame.KEYUP and (event.key == pygame.K_w or \
                event.key == pygame.K_s):
                walk_values[1] = 0
            if event.type == pygame.KEYUP and (event.key == pygame.K_d or \
                event.key == pygame.K_a):
                walk_values[0] = 0

        drew.walk(walk_values)


        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
