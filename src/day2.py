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

if __name__ == '__main__':
    state = initial_state_from_file(sys.argv[1])

    # part 1
    s1 = state.copy()
    s1[1] = 12
    s1[2] = 2
    compute(s1)
    print(f'value at s[0] after computing: {s1[0]}')

