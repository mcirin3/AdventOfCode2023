from collections import Counter

conv = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}

class Hand:
    def __init__(self, hand, bet):
        
        cpy = hand
        
        highest_hand = hand
        highest_type = 0
        for crd in conv.keys():
            
            test_hand = cpy.replace("J", crd)

            c = Counter([x for x in test_hand])
            
            t = list(sorted(c.values()))
            
            if t == [5] and highest_type <= 6:
                highest_type = 6
                highest_hand = test_hand
            elif t == [1, 4] and highest_type <= 5:
                highest_type = 5
                highest_hand = test_hand
            elif t == [2, 3] and highest_type <= 4:
                highest_type = 4
                highest_hand = test_hand
            elif t == [1, 1, 3] and highest_type <= 3:
                highest_type = 3
                highest_hand = test_hand
            elif t == [1, 2, 2] and highest_type <= 2:
                highest_type = 2
                highest_hand = test_hand
            elif t == [1, 1, 1, 2] and highest_type <= 1:
                highest_type = 1
                highest_hand = test_hand
            elif t == [1, 1, 1, 1, 1] and highest_type <= 0:
                highest_type = 0
                highest_hand = test_hand
                
        self.hand = highest_hand
        self.type = highest_type

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
