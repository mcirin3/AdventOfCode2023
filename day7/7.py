from collections import Counter

conv = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

class Hand:
    def __init__(self, hand, bet):

        c = Counter([x for x in hand])
        
        t = list(sorted(c.values()))
            
        if t == [5]:
            self.type = 6
        elif t == [1, 4]:
            self.type = 5
        elif t == [2, 3]:
            self.type = 4
        elif t == [1, 1, 3]:
            self.type = 3
        elif t == [1, 2, 2]:
            self.type = 2
        elif t == [1, 1, 1, 2]:
            self.type = 1
        elif t == [1, 1, 1, 1, 1]:
            self.type = 0


        self.bet = bet
        self.score = 0
        
        for i, v in enumerate(hand, start=1):
            self.score += (13 ** (5 - i)) * conv[v]

        self.score += (13 ** 5) * self.type

hands = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        a, b = line.split()
        hands.append(Hand(a, int(b)))
        
    hands.sort(key=lambda x: x.score, reverse=False)
    
total = 0

for i, hand in enumerate(hands, start=1):
    total += hand.bet * i
    
print(total)

