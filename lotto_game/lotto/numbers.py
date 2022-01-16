
"""
This is a base class used to generate randomly n numbers in a range 1-90.
The numbers can be generated when the class is initialized if n!=0 or using the genNumbers method.
"""
from random import sample


class TicketNumbers:

    def __init__(self, n: int = 0):
        if n != 0:
            self.numbers = sample(range(1, 91), n)
        else:
            self.numbers = [n]

    def genNumbers(self, nums):
        self.numbers = sample(range(1, 91), nums)

    def __str__(self):
        return ', '.join(str(n) for n in self.numbers)

