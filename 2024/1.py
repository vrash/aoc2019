with open('/Users/..../Desktop/Advent-Of-Code/2024/input.txt') as f:
    inputLines = f.read()

def calculate_list_distance(left_list, right_list):
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    total_distance = 0
    for num1, num2 in zip(sorted_left, sorted_right):
        distance = abs(num1 - num2)
        total_distance += distance
    
    return total_distance

def calculate_similarity_score(left_list, right_list):
    total_score = 0
    
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    for num in left_list:
        occurrences = right_counts.get(num, 0)
        score = num * occurrences
        total_score += score
        
    return total_score

def parse_input(input_text):
    left_list = []
    right_list = []
    
    for line in input_text.strip().splitlines():
        if line.strip():  
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))
    
    return left_list, right_list
    
print(calculate_list_distance(*parse_input(inputLines)))
print(calculate_similarity_score(*parse_input(inputLines)))