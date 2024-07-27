def play():
    from random import random
    brd = ([' ']*3,) + ([' ']*3,) + ([' ']*3,)
    res = 'Nobody'
    fin = False
    turn, not_turn = 'X', 'O'
    x1 = x2 = x_now = None
    print('Player1 starts first')
    while not fin:
        print('▬▬▬▬▬')
        if x_now != 0:
            print('1┃2┃3\
                 \n-╋-╋-\
                 \n4┃5┃6\
                 \n-╋-╋-\
                 \n7┃8┃9'\
                  )
        while True:
            if x1 != 0 and x1 != 1:
                x1 = input('Choose Player1 (AI/human) (enter "end" to end)')
                if x1 == '' or x1[0].upper() == 'A':
                    x1 = x_now = 0
                elif x1[0].upper() == 'H':
                    x1 = x_now = 1
                elif x1 == '"end"' or x1 == 'end':
                    fin = True
                    print('you have ended the game')
                    break
                else:
                    print('unrecognised input')
                    x1 = None
                    continue
            if x2 != 0 and x2 != 1:
                x2 = input('Choose Player2 (AI/human) (enter "end" to end)')
                if x2 == '' or x2[0].upper() == 'A':
                    x2 = 0
                elif x2[0].upper() == 'H':
                    x2 = 1
                elif x2 == '"end"' or x2 == 'end':
                    fin = True
                    print('you have ended the game')
                    break
                else:
                    print('unrecognised input')
                    x2 = None
                    continue
            if x_now == 1:
                x = input('Pick an empty position (enter "end" to end): ')
                if x == '"end"' or x == 'end':
                    fin = True
                    print('you have ended the game')
                    break
                try:
                    x = int(x) - 1
                    if x not in range(10):
                        print('There is no such position')
                        print('Positions are represented as shown above')
                    elif brd[x//3][x%3] != ' ':
                        print('That position is already occupied')
                    else:
                        x = (x//3, x%3)
                        break
                except:
                    print('Position is not recognised')
                    print('Please enter the position as a single digit integer only')
            else:
                x = aiplay(brd, turn)
                rand = int(len(x) * random())
                x = x[rand]
                break
        if fin:
            break
        brd[x[0]][x[1]] = turn
        turn, not_turn = not_turn, turn
        if x_now == x1:
            x_now = x2
        else:
            x_now = x1
        for i in range(3):
            if brd[i][0] == brd[i][1] == brd[i][2] != ' ' or brd[0][i] == brd[1][i] == brd[2][i] != ' ':
                res = brd[i][0] if brd[i][0] == brd[i][1] == brd[i][2] else brd[0][i]
                fin = True
                break
        if fin == False:
            if brd[0][0] == brd[1][1] == brd[2][2] != ' ' or brd[0][2] == brd[1][1] == brd[2][0] != ' ':
                res = brd[1][1]
                fin = True
            elif ' ' not in brd[0] + brd[1] + brd[2]:
                fin = True
        print(f'{brd[0][0]}┃{brd[0][1]}┃{brd[0][2]}\
                \n-╋-╋-\
                \n{brd[1][0]}┃{brd[1][1]}┃{brd[1][2]}\
                \n-╋-╋-\
                \n{brd[2][0]}┃{brd[2][1]}┃{brd[2][2]}'\
              )
    print(f'{res} Wins!')
    try:
        if input('play again? (Y/N)')[0].upper() == 'Y':
            return play()
    except:
        return play()
    print('game ended')

#################################### ai play ###################################

def aiplay(brd_cond = ([' ']*3,) + ([' ']*3,) + ([' ']*3,), turn = 0):
    p = brd_cond
#---------------------------------------------------------- Check if input is valid
    for i in range(3):
        if p[i][0] == p[i][1] == p[i][2] != ' '\
        or p[0][i] == p[1][i] == p[2][i] != ' ':
            return []
    if p[0][0] == p[1][1] == p[2][2] != ' '\
    or p[0][2] == p[1][1] == p[2][0] != ' '\
    or ' ' not in p[0] + p[1] + p[2]:
        return []
#---------------------------------------------------------- Assigns turns if needed
    if not (turn == 'X' or turn == 'O'):
        x = o = 0
        for i in brd_cond:
            for j in i:
                if j == 'X':
                    x += 1
                elif j == 'O':
                    o += 1
        if x > o:
            turn, not_turn = 'O', 'X'
        else:
            turn, not_turn = 'X', 'O'
    elif turn == 'X':
        not_turn = 'O'
    else:
        not_turn = 'X'
#------------------------------------------------------ Finds immediate and play
    dang = 0
    for i in range(3):
        t = nt = em = loc = count = 0
        for u in (p[i][0], p[i][1], p[i][2]):
            if u == turn:
                t += 1
                count += 1
            elif u == not_turn:
                nt += 1
                count += 1
            else:
                em += 1
                loc = count
        if em == 1 and (t == 2 or nt == 2):
            dang = (i, loc)
            if t == 2:
                return [dang]
    if dang != 0:
        return [dang]
    for i in range(3):
        t = nt = em = loc = count = 0
        for u in (p[0][i], p[1][i], p[2][i]):
            if u == turn:
                t += 1
                count += 1
            elif u == not_turn:
                nt += 1
                count += 1
            else:
                em += 1
                loc = count
        if em == 1 and (t == 2 or nt == 2):
            dang = (loc, i)
            if t == 2:
                return [dang]
    if dang != 0:
        return [dang]
    t = nt = em = loc = count = 0
    for u in (p[0][0], p[1][1], p[2][2]):
        if u == turn:
            t += 1
            count += 1
        elif u == not_turn:
            nt += 1
            count += 1
        else:
            em += 1
            loc = count
    if em == 1 and (t == 2 or nt == 2):
        return [(loc, loc)]
    t = nt = em = loc = count = 0
    for u in (p[0][2], p[1][1], p[2][0]):
        if u == turn:
            t += 1
            count += 1
        elif u == not_turn:
            nt += 1
            count += 1
        else:
            em += 1
            loc = count
    if em == 1 and (t == 2 or nt == 2):
        return [(loc, 2 - loc)]
#------------------------------------------------------ Plays double kills position
    res = gen_win(brd_cond, turn)
    if res:
        return res
#------------------------------------------------------ Deals with potential double kills positions
    pos_win = []
    pos_unk = []
    loses = False
    for i in range( len(brd_cond) ):
        for j in range( len(brd_cond[i]) ):
            if brd_cond[i][j] == ' ':
                brd_cond_dup = duplicate(brd_cond)
                brd_cond_dup[i][j] = turn
                res = find_immediate(brd_cond_dup, not_turn)
                if res:
                    brd_cond_dup[res[0][0]][res[0][1]] = not_turn
                t_turn, t_not_turn = not_turn, turn
                while res and not win_exists(brd_cond_dup, t_turn):
                    t_turn, t_not_turn = t_not_turn, t_turn
                    res = find_immediate(brd_cond_dup, t_turn)
                    if res:
                        brd_cond_dup[res[0][0]][res[0][1]] = t_turn
                if res or gen_win(brd_cond_dup, t_turn):
                    if t_turn == turn:
                        pos_win.append((i,j))
                    else:
                        continue
#-------------------------------------------------------- check for not_turn
                loses = False
                for n in range( len(brd_cond_dup) ):
                    for m in range( len(brd_cond_dup[n]) ):
                        if brd_cond_dup[n][m] == ' ':
                            brd_cond_dup2 = duplicate(brd_cond_dup)
                            brd_cond_dup2[n][m] = not_turn
                            res = find_immediate(brd_cond_dup2, turn)
                            if res:
                                brd_cond_dup2[res[0][0]][res[0][1]] = turn
                            t_turn, t_not_turn = turn, not_turn
                            while res and not win_exists(brd_cond_dup2, t_turn):
                                t_turn, t_not_turn = t_not_turn, t_turn
                                res = find_immediate(brd_cond_dup2, t_turn)
                                if res:
                                    brd_cond_dup2[res[0][0]][res[0][1]] = t_turn
                            if res or gen_win(brd_cond_dup2, t_turn):
                                if t_turn == not_turn:
                                    loses = True
                                    break
                    if loses:
                        break
                if not loses:
                    pos_unk.append((i,j))
    if pos_win:
        return pos_win
    else:
        return pos_unk

def find_immediate(p, turn):
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    for i in range(3):
        nt = em = loc = count = 0
        for u in (p[i][0], p[i][1], p[i][2]):
            if u == turn:
                nt += 1
                count += 1
            elif u == ' ':
                em += 1
                loc = count
        if em == 1 and nt == 2:
            return [(i, loc)]
    for i in range(3):
        nt = em = loc = count = 0
        for u in (p[0][i], p[1][i], p[2][i]):
            if u == turn:
                nt += 1
                count += 1
            elif u == ' ':
                em += 1
                loc = count
        if em == 1 and nt == 2:
            return [(loc, i)]
    nt = em = loc = count = 0
    for u in (p[0][0], p[1][1], p[2][2]):
        if u == turn:
                nt += 1
                count += 1
        elif u == ' ':
                em += 1
                loc = count
    if em == 1 and nt == 2:
            return [(loc, loc)]
    nt = em = loc = count = 0
    for u in (p[0][2], p[1][1], p[2][0]):
        if u == turn:
                nt += 1
                count += 1
        elif u == ' ':
                em += 1
                loc = count
    if em == 1 and nt == 2:
        return [(loc, 2 - loc)]

def gen_win(brd_cond, turn):
    res_set = []
    for i in range( len(brd_cond) ):
        for j in range( len(brd_cond[i]) ):
            if brd_cond[i][j] == ' ':
                brd_cond[i][j] = turn
                if win_exists(brd_cond, turn):
                    res_set.append((i, j))
                brd_cond[i][j] = ' '
    return res_set

def win_exists(p, turn):
    num = 0
    for i in range(3):
        t = em = 0
        for u in (p[i][0], p[i][1], p[i][2]):
            if u == turn:
                t += 1
            elif u == ' ':
                em += 1
        if em == 1 and t == 2:
            num += 1
    if num >= 2:
        return True
    for i in range(3):
        t = em = 0
        for u in (p[0][i], p[1][i], p[2][i]):
            if u == turn:
                t += 1
            elif u == ' ':
                em += 1
        if em == 1 and t == 2:
            num += 1
    if num >= 2:
        return True
    t = em = 0
    for u in (p[0][0], p[1][1], p[2][2]):
        if u == turn:
            t += 1
        elif u == ' ':
            em += 1
    if em == 1 and t == 2:
        num += 1
        if num >= 2:
            return True
    t = em = 0
    for u in (p[0][2], p[1][1], p[2][0]):
        if u == turn:
            t += 1
        elif u == ' ':
            em += 1
    if em == 1 and t == 2 and num == 1:
        return True
    else:
        return False

def duplicate(brd_cond):
    brd_cond_dup = list(brd_cond).copy()
    for i in range(3):
        brd_cond_dup[i] = list(brd_cond)[i].copy()
    return tuple(brd_cond_dup)

play()
