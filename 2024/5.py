
def parse_orderings() -> dict[int, set[int]]:
    ret = {}
    with open('5_input.txt') as f:
        for line in f:
            if line.strip():
                vals = line.strip().split('|')
                first = int(vals[0])
                second = int(vals[1])
                if first in ret:
                    ret[first].add(second)
                else:
                    ret[first] = set([second])
            else:
                break
    return ret

def parse_updates() -> list[list[int]]:
    skip_rows = True
    ret = []
    with open('5_input.txt') as f:
        for line in f:
            if line.strip() and skip_rows:
                continue
            elif line.strip() and not skip_rows:
                ret.append([int(i) for i in line.split(',')])
            if not line.strip():
                skip_rows = False
    return ret

def validate_update(update: list[int], orderings: dict[int, set[int]]) -> True:
    for i, page in enumerate(update):
        if page in orderings:
            for page_after in orderings[page]:
                try:
                    if update.index(page_after) <= i:
                        return False
                except ValueError:
                    continue
    return True


def get_middle(update: list[int]) -> int:
    return update[(len(update) // 2)]


def add_middle_valid(orderings, updates):
    return sum([get_middle(update) for update in updates if validate_update(update, orderings)])


def run():
    orderings = parse_orderings()
    print(orderings)

    updates = parse_updates()
    print(updates)

    print("SUM", add_middle_valid(orderings, updates))


if __name__ == "__main__":
    run()
