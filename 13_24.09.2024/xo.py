import os, random, time

# -------------------------Method 1----------------------------
print('Matrix')
matrix = [[str(x+y) for x in range(1, 4)] for y in range(0, 9, 3)]
print(matrix)
for x in matrix:
    print('|'.join(x))

print('Invers matrix')
invers_matrix = [[x[i] for x in matrix] for i in range(3)]
for x in invers_matrix:
    print('|'.join(x))

print('Diagonals matrix')
diagonals = [[x[abs(((len(matrix)-1)*j - i))] for (i, x) in enumerate(matrix)] for j in range(2)]
print(diagonals)

turn = {
    'x': 'o',
    'o': 'x'
}
player = 'x'
winner = ''
allow_cells = [str(i) for i in range(1, 10)]
finish = False
while not finish:
    for x in matrix:
        print('|'.join(x))
    isempty = False
    while not isempty:
        print(f'play {player}', end=': ')
        step = input()
        if ''.join(allow_cells).find(step) > -1:
            matrix[(int(step)-1)//3][(int(step)-1) % 3] = player
            allow_cells.remove(step)
            player = turn[player]
            isempty = True
        else :
            print(f'select only in {allow_cells}')
            pass
        time.sleep(0.1)
    invers_matrix = [[x[i] for x in matrix] for i in range(3)]
    diagonals = [[x[abs(((len(matrix)-1)*j - i))] for (i, x) in enumerate(matrix)] for j in range(2)]
    all_lists = matrix + invers_matrix + diagonals
    for l in all_lists:
        if len(set(l)) == 1:
            winner = l[0]       
            finish = True
            break
    
    print(chr(27) + "[2J")
    # time.sleep(0.5)
    
print(f'Winner: {winner}')