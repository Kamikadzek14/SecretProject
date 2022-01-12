def _update_balls(self) -> None:

    self._ticks_to_next_ball -= 1
    if self._ticks_to_next_ball <= 0:
        self._create_ball()
        self._ticks_to_next_ball = 20


    # Remove balls that fall below 1000 vertically
    balls_to_remove = [ball for ball in self._balls if ball.body.position.y > 10000]
    for ball in balls_to_remove:
        self._space.remove(ball, ball.body)
        self._balls.remove(ball)