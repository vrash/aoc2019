#!/usr/bin/python
# -*- coding: utf-8 -*-
#part one only using a dirty hack from reddit
filename = "/Users/..../Desktop/Advent-of-Code/2023/inputsmall.txt" 

rules, parts = open(filename).read().split("\n\n")

A, R  = lambda: 1 + x + m + a + s , lambda: 1
for r in rules.split():
  r = r.replace(':', ' and ')
  r = r.replace(',', '() or ')
  r = r.replace('{', '= lambda:')
  r = r.replace('}', '()')
  r = r.replace('in', '_in_')
  exec(r)
  #print(r)

sum = 0
for p in parts.split():
  p = p.replace(',',';')
  #print(p[1:-1]+';sum+=_in_()-1')
  exec(p[1:-1]+';sum+=_in_()-1')

print(sum)