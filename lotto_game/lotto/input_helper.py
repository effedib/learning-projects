
"""
Helper class created to manage and store the user inputs.
Creates 3 classes to manage:
-   Numbers to generate randomly = TicketNumbers
-   Bet type                     = Bet
-   City                         = City
The class require a "num" to mention when it asks an input to the user.
We can also decide the how many numbers to generate without using the "numInput" method.
"""

from lotto.numbers import TicketNumbers
from lotto.bet import Bet
from lotto.city import City


class InputHelper:
    def __init__(self, num=0, num2gen=0):
        self.numbers = TicketNumbers()
        self.bet = Bet()
        self.city = City()
        self.num = num
        self.num2gen = num2gen

    # the numInput method is used to return how many numbers have to be generated randomly.
    # After this, the class TicketNumbers generates the numbers.
    # The user has to choose a number between 1 and 10, 0 to exit.
    def numInput(self):
        while not 1 <= self.num2gen <= 10:
            try:
                self.num2gen = int(input(f'\nEnter how many numbers I have to generate for the bill n° {self.num}. '
                                         f'(MIN: 1 - MAX: 10 - 0: EXIT)\n'))
                if self.num2gen == 0:
                    print("Ending...")
                    exit()
            except ValueError:
                print("Enter a number between 1 and 10 (0 to EXIT)")

        self.numbers.genNumbers(self.num2gen)

        return self.numbers

    # the betInput method is used to return the type of the bet.
    def betInput(self):

        while not self.bet.is_allowed():
            bet_input = input(
                f"\nEnter the bet for the bill n° {self.num} (Enter 'help' to know the allowed types)\n").lower()

            self.bet.bet = bet_input

            # set the correct type using "self.bet.dict" where are stored the corrects types to select.
            try:
                if int(bet_input) <= self.num2gen:
                    self.bet.bet = self.bet.dict[bet_input]

            except:
                pass

            finally:
                # the __str__ Bet class magic method manages every type of input even if the input is wrong
                print(self.bet)

        return self.bet

    # the cityInput method is used to return the city selected from user.
    def cityInput(self):

        while not self.city.is_allowed():
            city_input = input(
                f"\nEnter the city of the bill n° {self.num} (Enter 'help' to know the allowed types)\n").lower()

            # set the correct city using "self.city.dict" where are stored the corrects cities to select.
            try:
                self.city.city = self.city.dict[city_input]

            # if the input is wrong, we have to store is anyway in self.city.city, then we can manage the error using
            # "print(self.city)"
            except:
                self.city.city = city_input

            finally:
                # the __str__ City class magic method manages every type of input even if the input is wrong
                print(self.city)

        return self.city
