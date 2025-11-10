import pygame

from luneth_engine import core


class Menu(core.State):
    def __init__(self):
        super().__init__("Menu")

    def get_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            print("→ Switching to Game")
            self.done = True

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("→ Exiting Game")
            self.done = True

    def draw(self, screen: pygame.Surface):
        screen.fill((5, 32, 74))
        pygame.display.set_caption("Game")
        pygame.display.flip()

    def update(self, screen: pygame.Surface, dt):
        super().update(screen, dt)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    # core systems
    settings = core.SharedSettings()
    tm = core.TimeManager()
    sm = core.StateManager()

    # set settings
    settings.add("fps", 60)

    # add states
    sm.add(Menu())
    sm.add(Game())
    sm.state.startup()

    running = True
    while running and sm.state:
        dt = clock.tick(settings.get("fps", 60)) / 1000.0  # seconds
        tm.update(dt)

        # event handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                sm.state.get_event(event)

        # update + draw
        sm.state.update(screen, dt)

        if sm.state.done:
            sm.next_state()
            if sm.state:
                sm.state.startup()
            else:
                running = False

    pygame.quit()


# --- Main Game Loop ---
if __name__ == "__main__":
    main()
