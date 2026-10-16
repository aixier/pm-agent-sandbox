class Counter:
    def __init__(self):
        self.n = 0
        self._history = []

    def inc(self, k=1):
        self.n += k
        self._history.append(self.n)
        return self.n

    def reset(self):
        self.n = 0
        self._history.clear()
        return self.n

    def dec(self, k=1):
        self.n -= k
        return self.n

    def history(self, last=None):
        h = list(self._history)
        return h if last is None else h[-last:]

    def clear_history(self):
        self._history.clear()

# note: reset helper pending
