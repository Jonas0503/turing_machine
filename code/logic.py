class TuringMachine:
    def __init__(self, alphabet: set, states: set, tape: list, instructions: list[tuple], start_state, end_state):
        self.alphabet = alphabet
        self.states = states
        self.tape = tape
        self.instructions = instructions
        self.start_state = start_state
        self.end_state = end_state

    def check_input(self) -> bool:
        if self.start_state not in self.states:
            print("The start state is not part of the states set.")
            return False

        if self.end_state not in self.states:
            print("The end state is not part of the states set.")
            return False

        for instruction in self.instructions:
            if len(instruction[0]) != 2 or len(instruction[1]) != 3:
                print("Wrong size for tuple in instructions.")
                return False

            if instruction[0][0] not in self.states or instruction[1][0] not in self.states:
                print("A state is not part of the states set.")
                return False

            if instruction[0][1] not in self.alphabet or instruction[1][1] not in self.alphabet:
                print("A symbol is not part of the alphabet.")
                return False

            if instruction[1][2] != "L" and instruction[1][2] != "R" and instruction[1][2] != "N":
                print("The direction must be defined as L, R or N.")
                return False

        for symbol_on_tape in self.tape:
            count = 0
            for symbol_in_alphabet in self.alphabet:
                if symbol_on_tape == symbol_in_alphabet:
                    break
                else:
                    count += 1

            if count == len(self.alphabet):
                print(f"The symbol {symbol_on_tape} is not part of the alphabet.")
                return False

        return True
