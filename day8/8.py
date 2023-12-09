from itertools import cycle
from math import lcm

def part1(lr, maps):
	print("Part 1:", trace('AAA', cycle(lr), maps))
def part2(lr,maps):
	currents = [x for x in maps.keys() if x[-1] == 'A']
	plens = [trace(current, cycle(lr), maps) for current in currents]

	print("Part 2:", lcm(*plens))

def trace(current, lr, maps): 
	plen = 0
	while current[-1] != 'Z':
		current = maps[current][next(lr)]
		plen += 1
	return plen

def readData(file_path):
	with open(file_path) as f:
		lines = f.read().splitlines()
	return lines[0], {z[:3]: {'L': z[7:10], 'R': z[12:15]} for z in lines[2:]}

def main():
	file_path = "input.txt"
	lr, maps = readData(file_path)
	part1(lr,maps)
	part2(lr,maps)

if __name__ == "__main__":
	main()

