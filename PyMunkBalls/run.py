import pygame

def run(self) -> None:


    # Main loop
    while self._running:
        # Progress time forward
        for x in range(self._physics_steps_per_frame):
            self._space.step(self._dt)

        self._process_events()
        self._update_balls()
        self._clear_screen()
        self._draw_objects()
        pygame.display.flip()
        # Delay fixed time between frames
        self._clock.tick(50)
    #  ?  pygame.display.set_caption("Fps: " + str(self._clock.get_fps()))