import re

f = open("input.txt", "r")
text = f.read()
pattern = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)')
res = pattern.findall(text)
sum = 0
enabled = True

for elem in res:
    if elem == 'do()':
        enabled = True
    elif elem == 'don\'t()':
        enabled = False
    else:
        if enabled:
            a , b = re.search(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', elem).groups()
            sum += int(a) * int(b)

print(sum)