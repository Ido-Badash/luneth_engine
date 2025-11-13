from abc import ABC, abstractmethod
from typing import Optional


class State(ABC):
    def __init__(self, name: str, game=None):
        self.name = name
        self.game = game
        self.done = False
        self.next: Optional[str] = None

    def startup(self):
        self.done = False

    def cleanup(self): ...

    @abstractmethod
    def get_event(self, event): ...

    @abstractmethod
    def draw(self, screen): ...

    @abstractmethod
    def update(self, screen, dt: float): ...
