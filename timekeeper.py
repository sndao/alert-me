import time
import datetime


class timekeeper:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.hour = self.now.hour
        self.minute = self.now.minute
        self.second = self.now.second
        self.start = 0
        self.timing = 0

    def start_time(self):
        self.start = time.time()
        return self.start

    def end_time(self):
        self.timing = time.time() - self.start
        return self.timing