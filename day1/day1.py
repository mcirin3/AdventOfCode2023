import sys 

f = open(sys.argv[1]).read().strip()
ans = 0 

for line in f.split('\n'):
    digits = []
    for i,c in enumerate(line): 
        if c.isdigit():
            digits.append(c) 
        for f, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']): 
            if line[i: ].startswith(val): 
                digits.append(str(f+1))
    score = int(digits[0]+digits[-1])
    ans += score 
print(score)
    