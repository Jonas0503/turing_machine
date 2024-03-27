import json
import sys
from code.logic import TuringMachine


def read_json() -> dict:
    # the second argument must be the file name
    if len(sys.argv) != 2:
        print("You must enter a filename and nothing more.")
        return

    data: dict = {}
    try:
        f = open(sys.argv[1])
        data = json.load(f)
    except FileNotFoundError:
        print("The file does not exist")
    except json.JSONDecodeError:
        print("The file is not a correct json file.")

    return data


# converts the dict to the right data types
def create_new_tm() -> TuringMachine:
    data = read_json()
    instructions_from_json: list = data["instructions"]

    tape: list = data["tape"]
    alphabet: set = set(data["alphabet"])
    states: set = set(data["states"])
    instructions: list[(tuple, tuple)] = []

    for instruction in instructions_from_json:
        instruction[0] = tuple(instruction[0])
        instruction[1] = tuple(instruction[1])
        instructions.append(tuple(instruction))

    return TuringMachine(alphabet, states, tape, instructions, data["start_state"], data["end_state"])


if __name__ == "__main__":
    tm = create_new_tm()
    tm.check_input()
    print(tm.eval_turing_machine(tm.start_state, 0))
