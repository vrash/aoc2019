def parse_input(input_text):
    rules_section, updates_section = input_text.strip().split('\n\n')
    rules = []
    for line in rules_section.splitlines():
        before, after = map(int, line.split('|'))
        rules.append((before, after))
    updates = []
    
    for line in updates_section.splitlines():
        update = list(map(int, line.strip().split(',')))
        updates.append(update)
    return rules, updates

def is_valid_order(update, rules):
    for before, after in rules:  
        if before in update and after in update:
            before_idx = update.index(before)
            after_idx = update.index(after)
            if before_idx > after_idx:
                return False
    return True

def sum_middle_values_of_valid_updates(rules, updates):
    total_sum = 0
    for update in updates:
        if is_valid_order(update, rules):
            total_sum += update[len(update) // 2]
    return total_sum

def reorder_update(update, rules):
    ordered_update = update[:]
    print(ordered_update)
    for before, after in rules:
        if before in ordered_update and after in ordered_update:
            print(before, after)
            before_idx = ordered_update.index(before)
            after_idx = ordered_update.index(after)
            if before_idx > after_idx:
                print(before_idx, after_idx, "yes")
                ordered_update[before_idx], ordered_update[after_idx] = ordered_update[after_idx], ordered_update[before_idx]
                print(ordered_update)
    if(is_valid_order(ordered_update, rules)):
        return ordered_update
    else:
        return reorder_update(ordered_update, rules)

def reorder_updates_and_sum_middle_values(rules, updates):
    total_sum = 0
    for update in updates:
        if is_valid_order(update, rules):
            continue
        else:
            ordered_update = reorder_update(update, rules)
            ordered_update = reorder_update(update, rules)
            total_sum += ordered_update[len(ordered_update) // 2]
    return total_sum

with open('/Users/../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()

rules, updates = parse_input(input_text)
valid_sum = reorder_updates_and_sum_middle_values(rules, updates)
print(valid_sum)