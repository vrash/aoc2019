#!/usr/bin/python
# -*- coding: utf-8 -*-
filename = "/Users/.../Desktop/Advent-of-Code/2023/input.txt" 
broadcasters = {}
conjunctions = {} 
flipflops = {} 
relevant = {} 
queue = {"rx"} 
low = 0 
high = 0 
button =0  
part1, part2 = 1, 1

with open(filename, "r") as file:

    for broadcaster, receivers in [x.split(" -> ") for x in file.read().splitlines()]:
        #print(broadcaster,receivers)
        b, receivers = broadcaster[1:], receivers.split(", ")
        
        if broadcaster == "broadcaster":  
          broadcasters[broadcaster] = {x : (lambda y: y) for x in receivers}
        
        elif broadcaster.startswith("&"): 
          broadcasters[b] = {x : (lambda y, b=b: set(conjunctions[b].values()) != {1}) for x in receivers}
          conjunctions[b] = {}
        
        elif broadcaster.startswith("%"): 
          broadcasters[b] = {x : (lambda y, b=b: flipflops[b]) for x in receivers}
          flipflops[b] = 0
    
    for k, v in broadcasters.items():
        for x in v:
            if x in conjunctions: 
              conjunctions[x][k] = 0
    
    while queue:
        current = queue.pop()
        relevant[current] = nxt = [k for k, v in broadcasters.items() if current in v]
        for x in nxt:
            if x not in relevant: queue.add(x)
    conj = {x for x in set(sum(relevant.values(), [])) if x in conjunctions}
    
    while conj:
        button += 1; 
        low += 1
        queue = [{"broadcaster" : (0, "button")}]
        
        while queue:    
            receiver, (signal, origin) = queue.pop(0).popitem()
            
            if receiver not in broadcasters: 
              continue
            
            if receiver in conjunctions: 
              conjunctions[receiver][origin] = signal

            if receiver in flipflops:
                if signal: 
                  continue
                else: 
                  flipflops[receiver] = not flipflops[receiver]

            for remote, signal_func in broadcasters[receiver].items():
                queue.append({remote : (sent := signal_func(signal), receiver)})
                if sent == 1: 
                  high += 1
                else:         
                  low += 1

            if receiver in conj and sent: 
              conj.remove(receiver) 
              part2 *= button
        
        if button == 1000: 
          part1 = low * high

print(part1, part2)

