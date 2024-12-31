from itertools import permutations

keypadSequences = open('small_input.txt').read().splitlines()

keypad = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '#': (3, 0), '0': (3, 1), 'A': (3, 2)
}
keypadBadPosition = (3,0)
startKeypad = (3, 2)

directionalpad = {
    '#': (0, 0), '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}
directionalpadBadPosition = (0,0)
startdirectionalpad = (0, 2)

def getNumericPart(code):
    return ''.join([elem for elem in code if elem.isdigit()])

def getdirections(drow, dcol):
    res = []
    if drow > 0:
        res.append('v'*drow)
    elif drow < 0:
        res.append('^'*abs(drow))
    if dcol > 0:
        res.append('>'*dcol)
    elif dcol < 0:
        res.append('<'*abs(dcol))
    return ''.join(res)

def getPossiblePermutations(pos, directions, position):
    perms = [sorted(directions), sorted(directions, reverse=True)]
    validPerms = []
    for perm in perms:
        if validatepath(pos, perm, position):
            validPerms.append(''.join(perm))
    return validPerms

def validatepath(pos, directions, position):
    _pos = pos
    for direction in directions:
        if direction == 'v':
            _pos = (_pos[0] + 1, _pos[1])
        elif direction == '^':
            _pos = (_pos[0] - 1, _pos[1])
        elif direction == '>':
            _pos = (_pos[0], _pos[1] + 1)
        elif direction == '<':
            _pos = (_pos[0], _pos[1] - 1)

        if _pos == position:
            return False
    return True

def getDirectionToWriteCode(input):
    pos = startKeypad
    result = []
    for elem in input:
        nextPos = keypad[elem]
        drow = nextPos[0] - pos[0]
        dcol = nextPos[1] - pos[1]
        directions = getdirections(drow, dcol)
        validPaths = getPossiblePermutations(pos, directions, keypadBadPosition)
        if len(result) == 0:
            for path in validPaths:
                result.append(path + 'A')
        elif len(result) >= 1:
            temp = []
            for res in result:
                for path in validPaths:
                    temp.append(res + path + 'A')
            result = temp
        pos = nextPos

    return result


def getDirectionToWriteDirection(input):
    pos = startdirectionalpad
    result = []
    for elem in input:
        nextPos = directionalpad[elem]
        drow = nextPos[0] - pos[0]
        dcol = nextPos[1] - pos[1]
        directions = getdirections(drow, dcol)
        validPaths = getPossiblePermutations(pos, directions, directionalpadBadPosition)
        if len(result) == 0:
            for path in validPaths:
                result.append(path + 'A')
        elif len(result) >= 1:
            temp = []
            for res in result:
                for path in validPaths:
                    temp.append(res + path + 'A')
            result = temp
        pos = nextPos

    min_length = min(len(r) for r in result)
    return [r for r in result if len(r) == min_length]

def getDirectionToWriteDirectionSample(input):
    pos = startdirectionalpad
    result = []
    for elem in input:
        nextPos = directionalpad[elem]
        drow = nextPos[0] - pos[0]
        dcol = nextPos[1] - pos[1]
        directions = getdirections(drow, dcol)
        validPaths = getPossiblePermutations(pos, directions, directionalpadBadPosition)[0]
        result.append(validPaths)
        result.append('A')
        pos = nextPos
    return ''.join(result)


def calculateComplexity(code):
    sol1 = getDirectionToWriteCode(code)
    sol2 = [elem for sol in sol1 for elem in getDirectionToWriteDirection(sol)]
    sol3 = [elem for sol in sol2 for elem in getDirectionToWriteDirection(sol)]
    print(sol3[0])
    print(sol2[0])
    print(sol1[0])
    print(code)
    min_length = min(len(r) for r in sol3)
    num = getNumericPart(code)
    print(f"Code: Numeric: {num}, minimum length: {min_length}")
    return min_length * int(num)

total = 0
for code in keypadSequences:
    score = calculateComplexity(code)
    total += score
    print()
print(total)

# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# <<vAA>A>^AvAA<^A>A<<vA>>^AvA^A<vA>^A<<vA>^A>AAvA^A<<vA>A>^AAAvA<^A>A
# code = '029A'
# sol1 = getDirectionToWriteCode(code)
# sol2 = getDirectionToWriteDirection(sol1)
# sol3 = getDirectionToWriteDirection(sol2)
# print(sol3)
# print(sol2)
# print(sol1)
# print(code)

# print(calculateComplexity("029A"))