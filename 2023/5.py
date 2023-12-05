#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
from collections import defaultdict

file_path = '/Users/.../Desktop/Advent-of-Code/2023/input.txt'  # Replace with the path to your input file


class SeedMapper:
    def __init__(self, mapping_instructions):
        self.mapping_rules = [[int(value) for value in line.split()] for line in mapping_instructions]

    def map_single_seed(self, seed):
        for (destination_start, source_start, size) in self.mapping_rules:
            if source_start <= seed < source_start + size:
                return seed + destination_start - source_start
        return seed

    def map_seed_ranges(self, seed_ranges):
        transformed_ranges = []
        for (dest_start, src_start, size) in self.mapping_rules:
            src_end = src_start + size
            updated_ranges = []
            while seed_ranges:
                (range_start, range_end) = seed_ranges.pop()
                before_range = (range_start, min(range_end, src_start))
                intersection_range = (max(range_start, src_start), min(src_end, range_end))
                after_range = (max(src_end, range_start), range_end)

                if before_range[1] > before_range[0]:
                    updated_ranges.append(before_range)
                if intersection_range[1] > intersection_range[0]:
                    transformed_ranges.append((intersection_range[0] - src_start + dest_start, intersection_range[1] - src_start + dest_start))
                if after_range[1] > after_range[0]:
                    updated_ranges.append(after_range)

            seed_ranges = updated_ranges

        return transformed_ranges + seed_ranges

def read_input(filepath):
    with open(filepath, 'r') as file:
        document_sections = file.read().strip().split('\n\n')

    initial_seeds, *mapping_sections = document_sections
    seeds_list = [int(num) for num in initial_seeds.split(':')[1].split()]
    seed_mappers = [SeedMapper(section.split('\n')[1:]) for section in mapping_sections]

    return seeds_list, seed_mappers

def find_lowest_location_number(filepath):
    seeds, mappers = read_input(filepath)

    # Solve Part 1: Individual Seed Mapping
    individual_mapped_seeds = []
    for seed in seeds:
        for mapper in mappers:
            seed = mapper.map_single_seed(seed)
        individual_mapped_seeds.append(seed)
    lowest_location_part1 = min(individual_mapped_seeds)
    print("Part 1 - Lowest Location Number:", lowest_location_part1)

    # Solve Part 2: Range Seed Mapping
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    mapped_ranges_results = []
    for start, size in seed_pairs:
        seed_ranges = [(start, start + size)]
        for mapper in mappers:
            seed_ranges = mapper.map_seed_ranges(seed_ranges)
        mapped_ranges_results.append(min(seed_ranges)[0])
    lowest_location_part2 = min(mapped_ranges_results)
    print("Part 2 - Lowest Location Number:", lowest_location_part2)

find_lowest_location_number(file_path)


