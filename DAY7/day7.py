
f = open('input.txt', 'r')
tests = []
numbers = []

def check(test, number):
    if len(test) == 1:
        return int(test[0]) == number
    else:
        return (check([str(int(test[0])+int(test[1]))]+test[2:], number) 
        or check([str(int(test[0])*int(test[1]))]+test[2:], number))

for line in f:
    tests.append(line.strip().split(':')[0])
    numbers.append(line.strip().split(':')[1].split(' ')[1:])

print(len(tests))
print(len(numbers))

sum = 0
for i in range(len(tests)):
    if check(numbers[i], int(tests[i])):
        sum += int(tests[i])

print(sum)