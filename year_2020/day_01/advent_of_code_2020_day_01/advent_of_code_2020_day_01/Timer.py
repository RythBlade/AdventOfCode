import time

class Timer:
    def __init__(self):
        self.startTime = time.perf_counter_ns()

    def start(self):
        self.startTime = time.perf_counter_ns()

    def elapsedTime_ns(self):
        return time.perf_counter_ns() - self.startTime

    def elapsedTime_ms(self):
        return (time.perf_counter_ns() - self.startTime) / 1000000.0

    def elapsedTime(self):
        return (time.perf_counter_ns() - self.startTime) / 1000000000.0