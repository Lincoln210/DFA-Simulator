import argparse
import sys

class DFA:
    def __init__(self, states, alphabet, start_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = self.start_state

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transitions:
            self.current_state = None
            return
        self.current_state = self.transitions[(self.current_state, input_value)]

    def in_accept_state(self):
        return self.current_state in self.final_states

    def go_to_initial_state(self):
        self.current_state = self.start_state

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            if self.current_state is None:
                return False
        return self.in_accept_state()

    def process_input(self, str):
        return self.run_with_input_list(str)

def create_dfa_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Read {len(lines)} lines from the file.")
            for i, line in enumerate(lines):
                print(f"Line {i + 1}: {line.strip()}")

            states = lines[1].split(':')[1].strip().split(' ')
            alphabet = lines[2].split(':')[1].strip().split(' ')
            start_state = lines[3].split(':')[1].strip()
            final_states = lines[4].split(':')[1].strip().split(' ')
            transitions = {}
            for line in lines[5:]:
                transition = line.split(':')[1].strip().split(' ')
                transitions[(transition[0], transition[1])] = transition[2]
            return DFA(states, alphabet, start_state, final_states, transitions)
    except Exception as e:
        print(f"Failed to create DFA from file: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description="DFA Simulator")
    parser.add_argument("-d", "--dfa", type=str, required=True, help="DFA definition file")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()

    dfa = create_dfa_from_file(args.dfa)
    if dfa is None:
        print("Could not create DFA. Exiting.")
        sys.exit(1)

    while True:
        try:
            input_string = input()
            result = dfa.run_with_input_list(input_string)
            print(f"{input_string} --> {'ACCEPT' if result else 'NOT ACCEPT'}")
        except EOFError:
            break




if __name__ == "__main__":
    main()


