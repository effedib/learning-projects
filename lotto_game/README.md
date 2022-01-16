# Learning Path 1

## Lotto ticket generator

Reproduces the generation of lotto tickets


## Requirements

- software architectures must be an OOP project
- software should ask how many bills the user want to generate (min: 1, max: 5, 0: exit)
- for each bill the software should ask the type of bill (ambata, ambo, terno, quaterna, cinquina) and the amount of numbers to generate (max 10 per bill)
- for each bill the software should ask the "city" (aka "ruota") of the bill: Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia and Tutte (for the project purpose completely ignore "ruota nazionale" and the "estratto determinato" play type).
- numbers will be randomly generated in the range 1-90 (inclusive)
- Print the generated tickets with nice ascii art table decoration (https://ozh.github.io/ascii-tables/)


## Start the software

```bash
python3 main.py -n {0,1,2,3,4,5}
```