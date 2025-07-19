class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.capacity >= self.size + n:
            self.size += n
        else:
            raise ValueError("Not enough space")

    def withdraw(self, n):
        if self.size >= n:
            self.size -= n
        else:
            raise ValueError("Not enough cookies")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

