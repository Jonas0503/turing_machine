# turing_machine

This is a turing machine with only one tape.


## How to use

To start the program create a json file like in [example.json](./example.json). The
alphabet there must always contain the underscore `"_"`. This is the empty symbol.

Then execute [main.py](/src/main.py) and a json file as a command line argument.
In the success case you will see the tape after all instructions and otherwise you
will see possible mistakes in your input.

In this example one is added to a binary number.

```
❯ python3 .\src\main.py .\example.json
['_', 1, 0, 1, 0, 1, 1, 0, 1, '_']
```
