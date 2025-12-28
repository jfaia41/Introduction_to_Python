class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("capacity must be a non-negative int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self._validate_n(n)
        if self._size + n > self._capacity:
            raise ValueError("deposit would exceed capacity")
        self._size += n

    def withdraw(self, n):
        self._validate_n(n)
        if n > self._size:
            raise ValueError("not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    def _validate_n(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative int")