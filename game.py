import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 60))
    pygame.display.set_caption("Test Game")
    pygame.mouse.set_visible(0)

    clock = pygame.time.Clock()
    going = True
    while going:
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
