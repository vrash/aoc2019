import time
import re
from collections import defaultdict

with open("/Users/vrashabhirde/Desktop/input.txt","r") as f:
	input =  [block.split("\n") for block in f.read().split("\n\n")]

def part1(input):
	rules = ''.join(input[0])
	tix = input[2][1:]
	rules = re.findall(r"([0-9]*)-([0-9]*)", rules) 
	numbers = set()
	for rule in rules:	
		for i in range(int(rule[0]), int(rule[1])+1):
			numbers.add(i)
	errors = []
	for ticket in tix: 
		for field in ticket.split(","): 
			if int(field) not in numbers: 
				errors.append(int(field)) 
	
	return sum(errors)

def part2(input):
	rules = ''.join(input[0]) 
	my_tix = input [1]
	tix = input[2][1:]
	rules = re.findall(r"([0-9]*)-([0-9]*)", rules)
	numbers = set()
	for rule in rules:
		for i in range(int(rule[0]), int(rule[1])+1):
			numbers.add(i)
	valid_ticket = []
	for ticket in tix:
		valid = True 
		for field in ticket.split(","):	
			if int(field) not in numbers:
				valid = False 
				break
		if valid: 
			valid_ticket.append(ticket)
	read_values_per_field = [set() for _ in range(len(valid_ticket[0].split(",")))] 
	for ticket in valid_ticket:
		for field in range(len(ticket.split(","))):
			read_values_per_field[int(field)].add(int(ticket.split(",")[field]))
	rules = []
	for x in input[0]:
		rules.append(re.findall(r"^(\w* *\w*):* *([0-9]*-[0-9]*) or ([0-9]*-[0-9]*)",x))

	rule_names = {}
	for i in range(len(rules)):
		name = rules[i][0][0]
		r1 = rules[i][0][1].split("-")
		r2 = rules[i][0][2].split("-")
		
		num_set = set() 
		for i in range(int(r1[0]), int(r1[1])+1): 
			num_set.add(i)
		for i in range(int(r2[0]), int(r2[1])+1):
			num_set.add(i)
		rule_names[name] = num_set

	sure = defaultdict(set)
	while len(sure) < len(read_values_per_field):
		maybe = defaultdict(set)
		for name, values in rule_names.items():
			for i in range(len(read_values_per_field)): 
				if i not in sure.values(): 
					if read_values_per_field[i].issubset(values): 
						maybe[name].add(i)
		for name, values in maybe.items(): 
			if len(values) == 1:	
				sure[name] = values.pop()
				del rule_names[name]
	my_tix_val = my_tix[1].split(",")
	
	ans = 1
	for key, value in sure.items(): 
		if key[0:3] == "dep":
			ans *= int(my_tix_val[value])
	return ans

print(part1(input))
print(part2(input))