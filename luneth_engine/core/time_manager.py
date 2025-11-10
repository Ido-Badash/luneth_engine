class TimeManager:
    def __init__(self):
        self.elapsed_time = 0.0
        self.dt = 0.0
        self.paused = False
        self.time_scale = 1.0
        self.timers = {}

    def update(self, dt):
        if self.paused:
            self.dt = 0.0
        else:
            self.dt = dt * self.time_scale
            self.elapsed_time += self.dt

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def reset(self):
        self.elapsed_time = 0.0
        self.dt = 0.0

    def add_timer(self, name: str, time: float):
        self.timers[name] = time

    def get_timer(self, name: str, default: float = 0.0):
        return self.timers.get(name, default)

    def set_timer(self, name: str, new_time: float):
        self.timers[name] = new_time

    def timer_done(self, name: str) -> bool:
        return self.elapsed_time >= self.timers.get(name, float("inf"))

    def timer_done_once(self, name: str) -> bool:
        if self.timer_done(name):
            self.timers.pop(name)
            return True
        return False

    def time_remaining(self, name: str) -> float:
        return max(self.get_timer(name), 0.0)
