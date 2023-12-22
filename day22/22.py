import sys
 
part = int(sys.argv[1]) if len(sys.argv) > 1 else 1
inType = sys.argv[2] if len(sys.argv) > 2 else "i"
inFile = "input.txt" if inType != "e" else "input.txt"
 
 
def simulateFall(bricks):
    n = len(bricks)
 
    supports = {i: [] for i in range(n)}
    supportedBy = {i: [] for i in range(n)}
 
    settled = {}
 
    for brick in bricks:
        end1, end2, bId = brick
        (x1, y1, z1), (x2, y2, z2) = end1, end2
 
        supporters = []
        while z1 > 1 and len(supporters) == 0:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    for z in range(z1, z2+1):
                        if (x, y, z-1) in settled:
                            supporters.append((x, y, z-1))
 
            if len(supporters) == 0:
                z1 -= 1
                z2 -= 1
 
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    settled[(x, y, z)] = bId
 
        for sId in set(settled[sup] for sup in supporters):
            supports[sId].append(bId)
            supportedBy[bId].append(sId)
 
    return supports, supportedBy
 
 
def countRemovable(supports, supportedBy):
    count = 0
    for bId in supports:
        canBeRemoved = True
        for sId in supports[bId]:
            if len(supportedBy[sId]) == 1:
                canBeRemoved = False
                break
 
        if canBeRemoved:
            count += 1
 
    return count
 
 
def countChainReaction(supports, supportedBy):
    count = 0
    for bId in supports:
        toCheck = supports[bId].copy()
        falling = {bId}
 
        while toCheck:
            curId = toCheck.pop(0)
 
            if all(sId in falling for sId in supportedBy[curId]):
                falling.add(curId)
                toCheck += supports[curId]
 
        count += len(falling) - 1
 
    return count
 
 
bricks = []
with open(inFile) as f:
    i = 0
    for line in f.readlines():
        brick = [[int(n) for n in end.split(",")]
                 for end in line.strip().split("~")]
        brick += [i]
 
        bricks.append(brick)
        i += 1
bricks.sort(key=lambda b: b[0][2])
 
 
if part == 1:
    supports, supportedBy = simulateFall(bricks)
 
    removable = countRemovable(supports, supportedBy)
 
    print(removable)
elif part == 2:
    supports, supportedBy = simulateFall(bricks)
 
    otherFalling = countChainReaction(supports, supportedBy)
 
    print(otherFalling)
