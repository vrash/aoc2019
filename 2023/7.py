#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from collections import Counter

card_strength = dict(zip('23456789TJQKA', range(13)))
card_strength_with_joker = dict(zip('J23456789TQKA', range(13)))

def part1(i):
    return sorted(Counter(i[0]).values(), reverse=True), [card_strength[c] for c in i[0]]

def part2(i):
    if i[0] == 'JJJJJ':
        hand = [5,]
    else:
        c = Counter(i[0])
        jokers = c.pop('J', 0)
        hand = sorted(c.values(), reverse=True)
        hand[0] += jokers

    return hand, [card_strength_with_joker[c] for c in i[0]]

data = [line.split() for line in open('/Users/.../Desktop/Advent-of-Code/2023/input.txt')]
print(sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted(data, key=part1))))
print(sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted(data, key=part2))))