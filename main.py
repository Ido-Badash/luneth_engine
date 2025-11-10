import pygame

from config import _config
from luneth_engine import core
from states_enum import States


class Menu(core.State):
    def __init__(self):
        super().__init__("Menu")

    def get_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            print("→ Switching to Game")
            self.done = True
            self.next = States.GAME

    def draw(self, screen: pygame.Surface):
        screen.fill((191, 172, 170))
        pygame.display.set_caption("Menu")
        pygame.display.flip()

    def update(self, screen: pygame.Surface, dt):
        super().update(screen, dt)


class Game(core.State):
    def __init__(self):
        super().__init__("Game")

    def get_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            print("→ Switching to Menu")
            self.done = True
            self.next = States.MENU

    def draw(self, screen: pygame.Surface):
        screen.fill((5, 32, 74))
        pygame.display.set_caption("Game")
        pygame.display.flip()

    def update(self, screen: pygame.Surface, dt):
        super().update(screen, dt)


def main():
    # states
    _states = [Menu(), Game()]

    # core systems
    ss = core.SharedSettings(_config)
    sm = core.StateManager(_states)
    tm = core.TimeManager()

    # init pygame
    pygame.init()
    screen = pygame.display.set_mode((ss.get("screen_w", 640), ss.get("screen_h", 480)))
    clock = pygame.time.Clock()

    # startup first state
    sm.state.startup()

    running = True
    while running and sm.state:
        dt = clock.tick(ss.get("fps", 60)) / 1000.0  # seconds
        tm.update(dt)

        # event handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                sm.state.get_event(event)

        # update + draw
        sm.state.update(screen, dt)

        # find and switch to the named state
        if sm.state.done:
            sm.default_switcher()

    pygame.quit()


# --- Main Game Loop ---
if __name__ == "__main__":
    main()
