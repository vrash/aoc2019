from itertools import tee
safetycount = 0

def is_sorted(lst):
    if len(lst) <= 1:
        return False
    nums = [int(x) for x in lst]
    is_decreasing = nums[1] < nums[0]
    
    for i in range(len(nums)-1):
        diff = nums[i] - nums[i+1] if is_decreasing else nums[i+1] - nums[i]

        if diff < 1 or diff > 3:
            return False
        if is_decreasing and nums[i] <= nums[i+1]:
            return False
        if not is_decreasing and nums[i] >= nums[i+1]:
            return False
    return True

def can_be_made_safe(lst):
    if is_sorted(lst):
        return True
    nums = [int(x) for x in lst]
    for i in range(len(nums)):
        test_list = nums[:i] + nums[i+1:]
        if is_sorted([str(x) for x in test_list]):
            return True
    return False


def parse_input(input_text):    
    global safetycount
    m = [line.strip().split() for line in input_text.strip().splitlines()]
    for line in m:
        print(line)
        if (can_be_made_safe(line)):
            print(line)
            print("true") 
            safetycount = safetycount + 1       

with open('/Users/Vrash.Irde/Desktop/Advent-Of-Code/2024/input.txt') as f:
    inputLines = f.read()

parse_input(inputLines)
print(safetycount)
