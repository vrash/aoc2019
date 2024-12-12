def countstones(count_stones, max_blinks):
    blink = 0
    while blink < max_blinks:
        newstones = {}
        for value, count in list(count_stones.items()):
            if value == 0:
                newstones[1] = newstones.get(1, 0) + count
            else:
                digit_count = len(str(value))
                if digit_count % 2 == 0:
                    divisor = 10 ** (digit_count // 2)
                    left = value // divisor
                    right = value % divisor
                    newstones[left] = newstones.get(left, 0) + count
                    newstones[right] = newstones.get(right, 0) + count
                else:
                    new_value = value * 2024
                    newstones[new_value] = newstones.get(new_value, 0) + count 
        count_stones = newstones
        blink += 1
    return sum(count for count in count_stones.values())

def solve(initial_stones, blinks):
    count_stones = {}
    for stone in initial_stones:
        count_stones[stone] = count_stones.get(stone, 0) + 1
    return countstones(count_stones, blinks)

input = [25, 17]
part1 = solve(input, 25)
print(part1)
part2 = solve(input, 75)
print(part2)
