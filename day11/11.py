def main():
    image = []
    count = 0
    with open('input.txt') as f:
        for i, line in enumerate(f):
            image.append([])
            for j, c in enumerate(line.strip()):
                if (c == '#'):
                    count += 1
                    image[i].append(count)
                else:
                    image[i].append(0)

    height = len(image)
    width  = len(image[0])
    free_rows = [0 for _ in range(height)]
    for i, line in enumerate(image):
        free_rows[i] = sum(line)
    
    free_cols = [0 for _ in range(width)]
    for i, line in enumerate(image):
        for j, c in enumerate(line):
            free_cols[j] += c
    
    leap_x = [1 if x == 0 else 0 for x in free_cols]
    leap_y = [1 if y == 0 else 0 for y in free_rows]
    leaps = (leap_x, leap_y)

    galaxies = []
    for y, line in enumerate(image):
        for x, thing in enumerate(line):
            if thing > 0:
                galaxies.append((x, y))

    print('part 1: ', end='')
    print_path_lengths(galaxies, leaps, 2)
    print('part 2: ', end='')
    print_path_lengths(galaxies, leaps, 1000000)
    

def print_path_lengths(galaxies: [(int, int)], leaps: ([int], [int]), leap_size: int):
    path_sum = 0
    for i, start_raw in enumerate(galaxies):
        for j, end_raw in enumerate(galaxies[i+1:]):
            start = translate_location(start_raw, leaps, leap_size)
            end   = translate_location(end_raw,   leaps, leap_size)
            diff = sub(end, start)
            path_len = abs(diff[0]) + abs(diff[1])
            # end_idx = i+1 + j
            # print(i+1, end_idx+1, path_len)
            path_sum += path_len
    print(path_sum)


def translate_location(loc: (int, int), leaps:([int], [int]), jump_size: int) -> (int, int):
    jump_count = (sum(leaps[0][:loc[0]]), (sum(leaps[1][:loc[1]])))
    jumps = scale(jump_size, jump_count)
    return add(sub(loc, jump_count), jumps)
    

def scale(s: int, a: (int, int)) -> (int, int):
    return (s * a[0], s * a[1])

def sub(a: (int, int), b: (int, int)) -> (int, int):
    return (a[0] - b[0], a[1] - b[1])

def add(a: (int, int), b: (int, int)) -> (int, int):
    return (a[0] + b[0], a[1] + b[1])

if __name__ == "__main__":
    main()

