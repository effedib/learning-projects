
"""
Business logic class.
Generates a number of tickets [num_bills] using a for loop and a static method "self.generator".
Every ticket is stored in a list "self.tickets".
The static method is used to generate every ticket, returns a new ticket (class: Ticket) using the bet, city and
numbers stored using the InputHelper class.
@num is the ticket num to create (i.e. enter the type for the ticket num 1)
"""

from lotto.ticket import Ticket
from lotto.input_helper import InputHelper


class Lotto:

    def __init__(self, num_bills):
        self.tickets = []
        for i in range(1, num_bills + 1):
            self.tickets.append(self.generator(i))

    @staticmethod
    def generator(num):

        user_input = InputHelper(num=num)
        user_input.numInput()
        user_input.betInput()
        user_input.cityInput()

        return Ticket(user_input.bet.bet, user_input.city.city, user_input.numbers.numbers)
