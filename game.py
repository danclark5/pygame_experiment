import pygame
from lib.util import load_image

def main():
    pygame.init()
    screen_flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((0, 0), screen_flags)
    pygame.mouse.set_visible(0)

    background, _ = load_image("main_bg.png")
    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
