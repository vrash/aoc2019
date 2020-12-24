from collections import defaultdict

with open("/Users/vrashabhirde/Desktop/input.txt") as f:
    input = f.read().strip("\n")

input = input.split("\n")
#Co-ordinates around point 0,0
#https://www.redblobgames.com/grids/hexagons/
co_ord = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]

def part1():
	tiles = defaultdict(lambda : False)
	for ln in input:
		hex = [0,0]
		while len(ln)>0:
			if ln[0] == 'e' or ln[0] == 'w':
				if ln[0] == 'e':
					hex[0] += 1
					hex[1] += 1
				else:
					hex[0] -= 1
					hex[1] -= 1
				ln = ln[1:]
			else:
				tk = ln[:2]
				ln = ln[2:]
				if tk == 'se':
					hex[1] += 1
				elif tk == 'ne':
					hex[0] += 1
				elif tk == 'nw':
					hex[1] -= 1
				elif tk == 'sw':
					hex[0] -= 1
		tiles[tuple(hex)] = not tiles[tuple(hex)]
	print("P1: ", sum(tiles.values()))
	return tiles

def updatetiles(tiles):
    w_tiles = defaultdict(lambda : False)
    count = defaultdict(lambda : 0)
    for x,y in tiles:
        if tiles[x,y]:
            for dx,dy in co_ord:
                nx,ny = x+dx,y+dy
                count[nx,ny] += 1

    lister = set(count.keys()).union(set(tiles.keys()))
    for x,y in lister:
        if tiles[x,y]:
            if count[x,y] == 0 or count[x,y] > 2:
                w_tiles[x,y] = False
            else:
                w_tiles[x,y] = True
        else:
            if count[x,y] == 2:
                w_tiles[x,y] = True
            else:
                pass
    return w_tiles

def part2(tiles):
	for _ in range(100):
		tiles = updatetiles(tiles)
	print("P2: ", sum(tiles.values()))

#lol
part2(part1())



