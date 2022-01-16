
"""
This is a base class used to define and print a ticket.
"""


class Ticket:

    def __init__(self, bet, city, numbers):
        self.type = bet
        self.city = city
        self.numbers = numbers

    def __str__(self):
        return "Numbers: {}\nBet type: {}\nCity: {}".format(', '.join(str(n) for n in self.numbers), self.type,
                                                            self.city)

    def ticket_print(self):
        print("""
    +-----------------------------------------------------+
    |{:^53}|
    +-----------------------------------------------------+
    | Numbers    |{:^40}|
    +-----------------------------------------------------+
    | Type       |{:^40}|
    +-----------------------------------------------------+
    | City       |{:^40}|
    +-----------------------------------------------------+
    """.format('T I C K E T', ', '.join(str(n) for n in self.numbers), self.type, self.city))
