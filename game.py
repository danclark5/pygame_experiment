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
    walk_values = {pygame.K_w: 0, pygame.K_a: 0, pygame.K_s: 0, pygame.K_d: 0}
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            elif event.type == pygame.KEYDOWN and event.key in walk_values.keys():
                walk_values[event.key] = 10

            elif event.type == pygame.KEYUP and event.key in walk_values.keys():
                walk_values[event.key] = 0

        drew.walk(walk_values, [])


        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
