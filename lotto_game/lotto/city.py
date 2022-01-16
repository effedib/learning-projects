
"""
This is a base class used to define and set the city.
"""


class City:

    def __init__(self, city: str = None):

        self.city = city
        self.dict = {'1': 'BARI', '2': 'CAGLIARI', '3': 'FIRENZE', '4': 'GENOVA',
                     '5': 'MILANO', '6': 'NAPOLI', '7': 'PALERMO', '8': 'ROMA',
                     '9': 'TORINO', '10': 'VENEZIA', '11': 'TUTTE'}

        if self.city in self.dict.keys():
            self.city = self.dict[city]

    def is_allowed(self):
        if self.city in self.dict.values():
            return True

        return False

    def __str__(self):
        if self.is_allowed():
            return f'City: {self.city}\n'

        elif self.city == 'help':
            return 'Cities allowed:\n1 = BARI / 2 = CAGLIARI / 3 = FIRENZE / 4 = GENOVA / 5 = MILANO\n6 = NAPOLI /' \
                   ' 7 = PALERMO / 8 = ROMA / 9 = TORINO / 10 = VENEZIA / 11 = TUTTE\n'

        else:
            return "City not allowed or missing\n"
