

def parse_input() -> list[list]:
    ret: list = []
    with open('2_input.txt') as f:
        for line in f:
            ret.append([int(item) for item in line.split(' ')])
    return ret

def is_increasing(levels: list) -> bool:
    return all(levels[i] <= levels[i+1] for i in range(len(levels) - 1))

def is_decreasing(levels: list) -> bool:
    return all(levels[i] >= levels[i+1] for i in range(len(levels) - 1))

def is_delta_in_range(levels: list) -> bool:
    return all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels) - 1))

def is_safe(levels: list) -> bool:
    return (is_increasing(levels) or is_decreasing(levels)) and is_delta_in_range(levels)

def remove_at_index(lst, index):
    """
    Returns a new list with the item at the specified index removed.

    Args:
        lst (list): The original list.
        index (int): The index of the item to remove.

    Returns:
        list: A new list with the specified item removed.
    """
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range")
    return lst[:index] + lst[index+1:]

def is_safe_v2(levels: list) -> bool:
    if is_safe(levels):
        return True
    else:
        for i in range(len(levels)):
            if is_safe(remove_at_index(levels, i)):
                return True
        return False

def count_safe(all_levels: list[list]):
    return sum(is_safe_v2(levels) for levels in all_levels)

def run():
    print(count_safe(parse_input()))


if __name__ == "__main__":
    run()
