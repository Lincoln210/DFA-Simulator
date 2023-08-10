# DFA-Simulator
# Overview
The DFASimulator is a Python program that simulates the behavior of a Deterministic Finite Automaton (DFA) based on the provided definition file. Users can input strings to see whether the DFA accepts or rejects the input.

# Features
DFA Creation: Define your DFA via a simple definition file.

String Testing: Input strings interactively and see if they're accepted or rejected by your DFA.

Debug Mode: Activate verbose mode for detailed insights.

# How to use:
### 1. Prepare your DFA definition file
Your DFA definition file should have the following format:
```
Number of lines
States: q0 q1 q2 ...
Alphabet: a b c ...
Start State: q0
Final States: q1 q2 ...
q0:a:q1
q0:b:q0
...
```

For instance, a DFA that accepts strings with an odd number of 'a's can be:

```
6
States: q0 q1
Alphabet: a
Start State: q0
Final States: q1
q0:a:q1
q1:a:q0
```

## 2. Run the Simulator
To run the simulator, use the following command:

```
python dfasimulator.py -d [path_to_dfa_definition_file]
```

## 3. Optional arguments
-v or --verbose: Enables verbose mode which provides more debugging information.

## 4. Input Strings to DFA
Once the simulator is running, input a string to check if the DFA accepts or rejects it. The result will be printed as either "ACCEPT" or "NOT ACCEPT".

To stop the simulator, simply input CTRL + D or CTRL + C.

# Error Handling
If the DFA definition file has any inconsistencies or errors, the program will alert the user.
If any unexpected error occurs, the program will print an error message and exit.

# Contributions
Feel free to fork this repository, submit issues or pull requests if you have improvements or features to suggest.
