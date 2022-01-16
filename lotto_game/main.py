
"""
This is the project's entrypoint, requires a number of tickets to generate using the argparse module.
To start the project launch from a Terminal: "python3 main.py -n [a number between 1 and 5 (0 to end the program)]"
"""

from argparse import ArgumentParser
from lotto.lotto import Lotto


def main():
    parser = ArgumentParser(description="Generate a number of lotto tickets defined by the user")

    parser.add_argument("-n", "--NumberTickets", type=int, choices=range(6), help="Number of bills to generate")

    args = vars(parser.parse_args())

    while True:

        if args["NumberTickets"] in range(1, 6):
            # generate a list of tickets using the Lotto class
            ticket_lst = Lotto(args["NumberTickets"])
            for ticket in ticket_lst.tickets:
                ticket.ticket_print()
            break

        elif args["NumberTickets"] == 0:
            print("Ending...")
            break

        else:
            print("Wrong Number of tickets. I'm quitting...")
            exit()


if __name__ == "__main__":
    main()
