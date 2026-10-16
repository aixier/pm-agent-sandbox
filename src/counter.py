class Counter:
    def __init__(self):
        self.n = 0

    def inc(self, k=1):
        self.n += k
        return self.n

    def reset(self):
        self.n = 0
        return self.n
