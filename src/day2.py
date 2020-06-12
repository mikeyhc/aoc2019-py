import sys

def initial_state_from_file(filename):
    with open(filename, 'r') as fh:
        data = fh.readlines()
    return list(map(int, data[0].split(',')))

def binary_op(fun, ip, state):
    state[state[ip+3]] = fun(state[state[ip+1]], state[state[ip+2]])

def compute(state):
    ip = 0
    while True:
        if state[ip] == 1:
            binary_op(lambda a, b: a + b, ip, state)
        elif state[ip] == 2:
            binary_op(lambda a, b: a * b, ip, state)
        elif state[ip] == 99:
            break
        ip += 4

def compute_with_args(state, noun, verb):
    state[1] = noun
    state[2] = verb
    compute(state)
    return state[0]

if __name__ == '__main__':
    state = initial_state_from_file(sys.argv[1])
    target = int(sys.argv[2])

    # part 1
    solution = compute_with_args(state.copy(), 12, 2)

    # part 2
    # determine the "base" value (noun and verb at 0)
    base = compute_with_args(state.copy(), 0, 0)

    # determine how much the 1 noun and verb changes the base
    noun_diff = compute_with_args(state.copy(), 1, 0) - base
    verb_diff = compute_with_args(state.copy(), 0, 1) - base

    # determine the amount of noun and verb require to make up the difference
    diff = target - base
    noun = diff // noun_diff
    verb = (diff % noun_diff) // verb_diff

    # sanity check
    assert target == compute_with_args(state.copy(), noun, verb)

    # output answers
    print(f'value at pos 0 after computing: {solution}')
    print(f'noun: {noun}; verb: {verb}')
