
"""
This is a base class used to define and set the bet type.
"""


class Bet:

    def __init__(self, bet: str = None):

        self.bet = bet
        self.dict = {'1': 'AMBATA', '2': 'AMBO', '3': 'TERNO', '4': 'QUATERNA', '5': 'CINQUINA'}

        if self.bet in self.dict.keys():
            self.bet = self.dict[bet]

    # check if "self.bet" is set correctly
    def is_allowed(self):
        if self.bet in self.dict.values():
            return True

        return False

    def __str__(self):
        if self.is_allowed():
            return f'Bet: {self.bet}\n'

        elif self.bet == 'help':
            return 'Bets allowed:\n1 = AMBATA / 2 = AMBO / 3 = TERNO / 4 = QUATERNA / 5 = CINQUINA\n'

        else:
            return "Bet not allowed, too big or missing!\n"
