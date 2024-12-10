

def parse_input() -> str:
    ret = str
    with open('3_input.txt') as f:
        ret = f.read()
    return ret

def valid_mul(mul: str) -> int:
    substr = mul[4:len(mul)-1]
    if "," not in substr:
        return 0

    a, b = tuple(substr.split(','))
    try:
        return int(a) * int(b)
    except ValueError:
        return 0

def calc_muls(muls) -> int:
    return sum(valid_mul(mul) for mul in muls)

def find_muls(text: str) -> list[str]:
    first_substr = "mul("
    last_substr = ")"
    activate_substr = "do()"
    deactivate_substr = "don't()"
    start = 0
    muls = []
    is_activated = True
    while start < len(text):
        next_dont = text.find(deactivate_substr, start)
        next_do = text.find(activate_substr, start)

        mul_start = text.find(first_substr, start)
        mul_end = text.find(last_substr, start + 4)
        if mul_start == -1 or mul_end == -1:
            break

        if is_activated and next_dont > 0 and (next_dont < mul_start):
            is_activated = False
            start = next_dont + len(deactivate_substr)
        elif not is_activated and next_do > 0 and (next_do < mul_start):
            is_activated = True
            start = next_do + len(activate_substr)
        else:
            if mul_end > mul_start + 12:
                start = mul_start + 4
            else:
                mul = text[mul_start:mul_end+1]
                if mul and is_activated:
                    muls.append(mul)
                start = mul_end + 1  # Move past the last found position
    return muls



def run():
    muls = find_muls(parse_input())
    print(calc_muls(muls))


if __name__ == "__main__":
    run()
