import pygame


def _process_events(self) -> None:

    #pause = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self._running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self._running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause()


###  Pause


def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h)).fill(pygame.Color("blue"))

        font = pygame.font.Font('freesansbold.ttf', 70)
        text = font.render('PAUSED', True, (0, 255, 0), (255, 69, 0))

        textRect = text.get_rect()

        textRect.center = (pygame.display.Info().current_w // 2, pygame.display.Info().current_h // 4)

        pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h)).blit(text, textRect)
        pygame.display.flip()





        #message_to_screen("Paused", black, 100, size="large")
        # message_to_screen("Press c to press q to", black, 25)
        # pygame.display.update()
        # self.clock.tick(5)

