# The Merchants Guide To to the galaxy

Percival you have to enter an unit of measure, the value has to be in Roman number format: "glob is I", means "glob=1".
You can continue with others units of measure as you want.

After you can define the cost of a metal: glob glob Silver is 34 Credits, set the cost of Silver to 17.
You can define the cost of the metal you want but you have to use a unit of measure already defined previously.

You can sum the units of measure previously defined, the following is legal: how much is pish tegj glob glob ?

You can ask how many credits like this: how many Credits is glob prok Silver ? .

## Installation

Use the Dockerfile to generate a project image and run a container or download it from [Docker Hub](https://hub.docker.com/repository/docker/francescodb86/td-challenge).


## How to run

```bash
python3 main.py
```

```python
# set an unit of measure
glob is I

# define the cost of a metal
glob glob Silver

# sum the units of measure previously defined
how much is pish tegj glob glob?

# ask how many credits
how many Credits is glob prok Silver?
```