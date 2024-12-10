from collections import Counter

class LocationLists:
    list1: list
    list2: list
    counter: Counter

    def __init__(self):
        self.list1 = []
        self.list2 = []

    def append_left(self, item: int) -> None:
        self.list1.append(item)

    def append_right(self, item: int) -> None:
        self.list2.append(item)

    def sort_lists(self):
        self.list1.sort(reverse=True)
        self.list2.sort(reverse=True)

    def count(self):
        return Counter(self.list2)




def parse_input() -> LocationLists:
    locations = LocationLists()
    with open('1_input.txt') as f:
        for line in f:
            items = line.split('   ')
            item1 = int(items[0].strip())
            item2 = int(items[1].strip())
            locations.append_left(item1)
            locations.append_right(item2)
    locations.sort_lists()
    return locations

def calc_distance(locations: LocationLists):
    total = 0
    for i in range(len(locations.list1)):
        diff = locations.list1[i] - locations.list2[i]
        total += abs(diff)
    return total

def count_similarity(locations: LocationLists):
    total = 0
    counter = locations.count()
    for item in locations.list1:
        total += item * counter[item]
    return total


def run():
    locations: LocationLists = parse_input()
    print("distance", calc_distance(locations))
    print("similarity", count_similarity(locations))


if __name__ == "__main__":
    run()
