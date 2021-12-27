from main.input import InputBot


def main():
    while True:
        print_help = """
Percival you have to enter a unit of measure, the value has to be in Roman number format: glob is I, means glob=1
You can continue with others units of measure as you want.

After you can define the cost of a metal: glob glob Silver is 34 Credits, set the cost of Silver to 17.
You can define the cost of the metal you want but you have to use a unit of measure already defined previously.

You can sum the units of measure previously defined, the following is legal: how much is pish tegj glob glob ?

You can ask how many credits like this: how many Credits is glob prok Silver ? 
        """
        user_input = input("Enter the input (BLANK to quit): ")
        if user_input.lower() == "":
            print("Bye bye!")
            break

        elif user_input.lower() == "help":
            print(print_help)
            continue

        try:
            prefix, suffix = user_input.lower().split(" is ")
            robot = InputBot(prefix, suffix)
            print(robot.checkInput())

        except:
            print("I have no idea what you are talking about\n")


if __name__ == "__main__":
    main()
