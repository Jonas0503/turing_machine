class TuringMachine:
    def __init__(self, alphabet: set, states: set, tape: list, instructions: list[(tuple, tuple)], start_state, end_state) -> None:
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
                print("Wrong size for a tuple in instructions.")
                return False

            if instruction[0][0] not in self.states or instruction[1][0] not in self.states:
                print("A state in the instructions is not part of the states set.")
                return False

            if instruction[0][1] not in self.alphabet or instruction[1][1] not in self.alphabet:
                print("A symbol in the instructions is not part of the alphabet.")
                return False

            if instruction[1][2] != "L" and instruction[1][2] != "R" and instruction[1][2] != "N":
                print(f"The direction {instruction[1][2]} in the instructions must be defined as L, R or N.")
                return False

        for symbol_on_tape in self.tape:
            count = 0
            for symbol_in_alphabet in self.alphabet:
                if symbol_on_tape == symbol_in_alphabet:
                    break
                else:
                    count += 1

            if count == len(self.alphabet):
                print(f"The symbol {symbol_on_tape} on the tape is not part of the alphabet.")
                return False

        return True


    def eval_turing_machine(self, state, position: int = 0) -> list:
        symbol_on_tape = self.tape[position]
        for instruction in self.instructions:
            if instruction[0][0] == state and symbol_on_tape == instruction[0][1]:
                self.tape[position] = instruction[1][1]
                state = instruction[1][0]

                if position == 0 and instruction[1][2] == "L":
                    self.tape.insert(0, "_")
                elif position == len(self.tape)-1 and instruction[1][2] == "R":
                    self.tape.append("_")
                    position += 1
                else:
                    if instruction[1][2] == "L":
                        position -= 1
                    elif instruction[1][2] == "R":
                        position += 1
                break

        if state == self.end_state:
            return self.tape
        else:
            return self.eval_turing_machine(state, position)


if __name__ == "__main__":
    # example
    tape = [1, 0, 1, 0, 1, 1, 0, 0]
    alphabet = {"_", 0, 1}
    states = {"a", "b", "c", "d"}
    instructions = [(("a", 1), ("a", 1, "R")),
                    (("a", 0), ("a", 0, "R")),
                    (("a", "_"), ("d", "_", "L")),
                    (("c", 0), ("c", 0, "L")),
                    (("c", 1), ("c", 1, "L")),
                    (("c", "_"), ("b", "_", "R")),
                    (("d", 0), ("c", 1, "L")),
                    (("d", 1), ("d", 0, "L")),
                    (("d" "_"), ("b", 1, "N"))]

    tm = TuringMachine(alphabet, states, tape, instructions, "a", "b")
    print(tm.eval_turing_machine(tm.start_state, 0))
