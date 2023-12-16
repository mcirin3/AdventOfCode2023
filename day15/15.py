import re 
from functools import reduce

def deerHash(s: str) -> int: 
	return reduce(lambda h, c: ((h + ord(c)) * 17) % 256, s, 0)
def readData() -> str:
	with open('input.txt') as f:
		return f.read().strip()
def part1():
	print("1:", sum(deerHash(x) for x in readData().split(',')))

def part2():
	boxes = [{} for i in range(256)]
	for x in readData().split(','):
		label = re.match(r'^[a-z]+', x).group(0)
		box = boxes[deerHash(label)]
		if '=' in x: 
			box[label] = int(x.split('=')[1])
		else: 
			box.pop(label, None)
	print("2:", sum((k+1)*(i+1)*v 
		      for k,v in enumerate(boxes)
		      for i,v in enumerate(v.values())))
		

part1()
part2()
