import fileinput
import re
from collections import defaultdict

food = []
input = list([l.strip() for l in fileinput.input()])

for lines in input:
    first, rest = lines.split('(contains ')
    ingredients = set(first.split())
    allergens = set(rest[:-1].split(', '))
    food.append((ingredients,allergens))

ingredients = set()
allergens = set()

for ing,all in food:
    ingredients |= all
    allergens |= ing

intersect = {i: set(allergens) for i in ingredients}

cdict = defaultdict(int)
for ing,all in food:
    for i in ing:
        intersect[i] += 1
    for a in all:
        for i in ingredients:
            if i not in ing:
                intersect[i].discard(a)

map_ingredients = {}
set_used = set()

not_allergen_count = 0
for i in ingredients:
    if not intersect[i]:
        not_allergen_count += cdict[i]
#part 1
print(not_allergen_count)

while len(map_ingredients) < len(allergens):
    for i in ingredients:
        _possible = [a for a in intersect[i] if a not in set_used]
        if len(_possible)==1:
            map_ingredients[i] = _possible[0]
            set_used.add(_possible[0])
#canon sort
canonical = ','.join([k for k,v in sorted(map_ingredients.items(), key=lambda kv:kv[1])])
#part 2
print(canonical)