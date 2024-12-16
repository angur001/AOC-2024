f = open("input.txt")
machines = [elem.split("\n") for elem in f.read().split("\n\n")]

def find_solution(A_button, B_button, prize):
    X_a, Y_a = A_button
    X_b, Y_b = B_button
    X_prize, Y_prize = prize
    X_prize += 10000000000000
    Y_prize += 10000000000000
    b = (X_prize * Y_a - Y_prize * X_a) / (X_b * Y_a - X_a * Y_b)
    a = (X_prize * Y_b - Y_prize * X_b) / (X_a * Y_b - X_b * Y_a)
    if (int(a) == a and int(b) == b):
        return (a,b)
    return ()

def get_cost(solution):
    return solution[0]*3 + solution[1]


total = 0
for machine in machines:
    A_button = tuple([int(text[3:]) for text in machine[0].split(":")[1].split(",")])
    B_button = tuple([int(text[3:]) for text in machine[1].split(":")[1].split(",")])
    prize = tuple([int(text[3:]) for text in machine[2].split(":")[1].split(",")])
    solution = find_solution(A_button, B_button, prize)
    if solution != ():
        cost = get_cost(solution)
        total += cost

print(total)




