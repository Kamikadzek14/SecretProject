
import pygame


background_image1 = pygame.image.load("Graphic\Background1.png")
background_image2 = pygame.image.load("Graphic\Background2.png")


def _clear_screen(self, globe: int) -> None:
    """
    Clears the screen.
    :return: None
    """
    if globe == 1:
        background_image = pygame.transform.scale(background_image1, (pygame.display.Info().current_w, pygame.display.Info().current_h))
        self._screen.blit(background_image, [0, 0])
    elif globe == 2:
        background_image = pygame.transform.scale(background_image2, (pygame.display.Info().current_w, pygame.display.Info().current_h))
        self._screen.blit(background_image, [0, 0])
