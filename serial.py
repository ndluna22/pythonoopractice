"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new generator, starting at start."""

        self.start = start  # self.a
        self.next = start  # self.b

    def generate(self):
        """Return next serial."""

        self.next += 1  # adds 1 every time
        return self.next - 1  # starts at 100 instead of 101

    def reset(self):
        """Reset number to original start."""

        self.next = self.start  # next number will be self.a, start
