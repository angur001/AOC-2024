import re

f = open("input.txt", "r")
text = f.read()
pattern = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
sum = 0

for match in pattern.finditer(text):
    sum += int(match.group(1)) * int(match.group(2))

print(sum)