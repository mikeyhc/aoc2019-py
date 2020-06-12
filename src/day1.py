import sys

def fuel_total_cost(mass):
    total_cost = fuel_cost(mass)
    new_cost = fuel_cost(total_cost)
    while new_cost > 0:
        total_cost += new_cost
        new_cost = fuel_cost(new_cost)
    return total_cost

def fuel_cost(mass):
    return mass // 3 - 2

def fuel_from_file(filename):
    with open(filename, 'r') as fh:
        masses = map(lambda x: int(x.strip()), fh.readlines())

    # I would use a reduce here, but skipped it to keep it simple
    mass_fuel = 0
    total_fuel = 0
    for mass in masses:
        mass_fuel += fuel_cost(mass)
        total_fuel += fuel_total_cost(mass)
    return mass_fuel, total_fuel

if __name__ == '__main__':
    mass, total = fuel_from_file(sys.argv[1])
    print(f'fuel cost for mass: {mass}')
    print(f'total fuel cost including fuel: {total}')

