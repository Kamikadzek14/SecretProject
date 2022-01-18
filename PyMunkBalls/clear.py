
import pygame


background_image = pygame.image.load("Graphic\Background.png")
background_image = pygame.transform.scale(background_image, (pygame.display.Info().current_w, pygame.display.Info().current_h))


def _clear_screen(self) -> None:
    """
    Clears the screen.
    :return: None
    """
    self._screen.blit(background_image, [0,0])

