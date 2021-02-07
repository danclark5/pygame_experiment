import os
import pygame
from pygame.compat import geterror

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:", fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

def main():
    pygame.init()
    screen_flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((0, 0), screen_flags)
    pygame.display.set_caption("Test Game")
    pygame.mouse.set_visible(0)

    background, _ = load_image("main_bg.png")
    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    going = True
    while going:
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
