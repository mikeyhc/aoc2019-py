def _make_wire(parts):
    horizontal, vertical = [], []
    x, y = 0, 0
    for part in parts:
        direction = part[:1]
        distance = int(part[1:])
        if direction == 'U':
            vertical.append(((x, y), distance))
            y += distance
        elif direction == 'D':
            vertical.append(((x, y), -distance))
            y -= distance
        elif direction == 'R':
            horizontal.append(((x, y), distance))
            x += distance
        elif direction == 'L':
            horizontal.append(((x, y), -distance))
            x -= distance
        else:
            raise ValueError
    return (horizontal, vertical)


def wires_from_file(filename):
    wires = []
    with open(filename, 'r') as fh:
        for line in fh:
            wires.append(_make_wire(line.split(',')))
    return wires

def intersects(h, v):
    ((hx, hy), hd) = h
    ((vx, vy), vd) = v

    if hd < 0:
        x1, x2 = hx + hd, hx
    else:
        x1, x2 = hx, hx + hd

    if vd < 0:
        y1, y2 = vy + vd, vy
    else:
        y1, y2 = vy, vy + vd

    if x1 <= vx <= x2 and y1 <= hy <= y2:
        return (vx, hy)
    return None

def find_intersections(horizontal, vertical):
    intersections = []
    for h in horizontal:
        for v in vertical:
            i = intersects(h, v)
            if i:
                intersections.append(i)
    return intersections

def find_nearest_part(w1, w2):
    (h1, v1) = w1
    (h2, v2) = w2

    intersections = find_intersections(h1,v2) + find_intersections(h2, v1)
    return min(map(lambda p: abs(p[0]) + abs(p[1]), intersections))

def solve(filename):
    w1, w2 = wires_from_file(filename)
    print(find_nearest_part(w1, w2))
