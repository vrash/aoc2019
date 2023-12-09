#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

file_path = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 
with open(file_path, 'r') as file:
    histories = [list(map(int, line.strip().split())) for line in file.readlines()]

def extrapolate(history,part1):
    seq = [history]
    while seq[-1].count(0) != len(seq[-1]):
        cur_seq = seq[-1]
        next_sequence = [cur_seq[i + 1] - cur_seq[i] for i in range(len(cur_seq) - 1)]
        seq.append(next_sequence)

    if part1:
        for i in range(len(seq) - 2, -1, -1):
            seq[i].append(seq[i][-1] + seq[i + 1][-1])
        return seq[0][-1]
    else:
        seq[-1].insert(0, 0)
        for i in range(len(seq) - 2, -1, -1):
            seq[i].insert(0, seq[i][0] - seq[i + 1][0])
        return seq[0][0]

#print1
print(sum(extrapolate(history,True) for history in histories))

#print2
print(sum(extrapolate(history,False) for history in histories))

