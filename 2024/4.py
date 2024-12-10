
def parse_input() -> list[str]:
    ret = []
    with open('4_input.txt') as f:
        for line in f:
            ret.append(line)
    return ret

def get_directions():
    directions = []
    for yi, xi in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        direction = []
        for j in [0, 1, 2, 3]:
            direction.append((yi*j, xi*j))
        directions.append(direction)
    return directions


def valid_char(matrix, y_ix, x_ix) -> bool:
    if y_ix >= 0 and y_ix < len(matrix):
        if x_ix >= 0 and x_ix < len(matrix[y_ix]):
            return True
    return False


def check_direction(matrix, y_ix, x_ix, direction) -> int:
    word = 'XMAS'
    dy_m, dx_m = direction[1]
    dy_a, dx_a = direction[2]
    dy_s, dx_s = direction[3]
    if matrix[y_ix][x_ix] != 'X':
        return 0
    if not valid_char(matrix, y_ix+dy_m, x_ix+dx_m) or matrix[y_ix+dy_m][x_ix+dx_m] != 'M':
        return 0
    if not valid_char(matrix, y_ix+dy_a, x_ix+dx_a) or matrix[y_ix+dy_a][x_ix+dx_a] != 'A':
        return 0
    if not valid_char(matrix, y_ix+dy_s, x_ix+dx_s) or matrix[y_ix+dy_s][x_ix+dx_s] != 'S':
        return 0
    print('found', y_ix, x_ix, direction)
    return 1

def check_cross(matrix, y_ix, x_ix) -> int:
    if matrix[y_ix][x_ix] != 'A':
        return 0
    if not valid_char(matrix, y_ix-1, x_ix-1) or not valid_char(matrix, y_ix+1, x_ix+1):
        return 0
    if not valid_char(matrix, y_ix+1, x_ix-1) or not valid_char(matrix, y_ix-1, x_ix+1):
        return 0

    part1 = matrix[y_ix-1][x_ix-1] + matrix[y_ix+1][x_ix+1]
    part2 = matrix[y_ix+1][x_ix-1] + matrix[y_ix-1][x_ix+1]

    if 'M' in part1 and 'S' in part1 and 'M' in part2 and 'S' in part2:
        return 1
    else:
        return 0



def get_xmas_count(matrix):
    directions = get_directions()
    total = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            for d in directions:
                total += check_direction(matrix, y, x, d)
    return total


def get_mas_count(matrix) -> int:
    total = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            total += check_cross(matrix, y, x)
    print(total)
    return total



def run():
    matrix = parse_input()
    print(get_mas_count(matrix))


if __name__ == "__main__":
    run()
