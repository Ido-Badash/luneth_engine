from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, name: str):
        self.name = name
        self.done = False
        self.next: State = None
        self.previous: State = None

    def startup(self):
        pass

    @abstractmethod
    def get_event(self, event):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self, screen, dt: float):

        self.draw(screen)
