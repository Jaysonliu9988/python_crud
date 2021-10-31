import json

# This function repeatedly prompts for input until an integer is entered.
def input_int(prompt):
    while True:
        target = input(prompt)
        try:
            return int(target)
        except:
            print('Need to enter an integer.')
            continue

def input_something(prompt):
    while True:
        char_target = input(prompt).strip()
        if not char_target:
            print('Enter a valid string, which cannot be composed of blank keys and tabs.')
        else:
            return char_target

