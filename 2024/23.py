from collections import defaultdict
from pathlib import Path

def solve(text):
    graph = defaultdict(set)
    nodes = set()
    for line in text.splitlines():
        if line.strip():
            a, b = line.strip().split('-')
            graph[a].add(b)
            graph[b].add(a)
            nodes.add(a)
            nodes.add(b)
    
    triplets = set()
    for node in graph:
        for n1 in graph[node]:
            for n2 in graph[node]:
                if n1 < n2 and n2 in graph[n1]:
                    triplets.add(tuple(sorted([node, n1, n2])))
    
    max_clique = set()
    for node in nodes:
        clique = {node}
        possible = graph[node].copy()
        
        while possible:
            next_node = possible.pop()
            can_add = True
            for c in clique:
                if next_node not in graph[c]:
                    can_add = False
                    break
            if can_add:
                clique.add(next_node)
                
        if len(clique) > len(max_clique):
            max_clique = clique
    
    return sum(1 for t in triplets if any(n.startswith('t') for n in t)), ','.join(sorted(max_clique))

p1, p2 = solve(Path("/Users/...p/Advent-Of-Code/2024/input.txt").read_text())
print(p1)
print(p2)