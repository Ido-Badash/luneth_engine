from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, name: str):
        self.name = name
        self.done = False
        self.next: str = None
        self.previous: str = None

    def startup(self): ...

    @abstractmethod
    def get_event(self, event): ...

    @abstractmethod
    def draw(self, screen): ...

    @abstractmethod
    def update(self, screen, dt: float):
        self.draw(screen)
