import time
import math
import random

class SolveTime:
    def __init__(self, t):
        self.min = math.floor(t / 60)
        self.sec = math.floor(t % 60)
        self.ms = math.floor((t % 1) * 1000)
    def __repr__(self):
        return f'{self.min}m {self.sec}s {self.ms}ms'


class Move:
    def __init__(self, loc='none', mod=''):
        self.loc = loc
        self.mod = mod
        if self.loc in 'RML':
            self.loc_class = 0
        else:
            self.loc_class = 1
    def checkGood(self, m):
        return self.loc_class != m.loc_class
    def setLoc(self, loc):
        self.loc = loc
    def setMod(self, mod):
        self.mod = mod
    def __repr__(self):
        return f'{self.loc}{self.mod}'


def genScramble(n):
    moves = ['R', 'M', 'U', 'L', 'D']
    movelist = []
    s = len(moves)
    last = 'null'
    move = 'null'
    for _ in range(n):
        while move == last:
            i = random.randrange(s)
            move = moves[i]
            m = random.randrange(3)
            if m == 1:
                move += "'"
            if m == 2:
                move += '2'
        last = move
        movelist.append(move)
    print(' '.join(movelist))


def stop_watch():
    input('Enter to START')
    start = time.time()
    input('Enter to STOP')
    end = time.time()
    t = SolveTime(end - start)
    print(f'The time was: {t}')
    return t


def start():
    user_input = ""
    times = open('times.txt', 'a')
    while user_input != 'q':
        genScramble(30)
        t = stop_watch()
        times.write(f'{t}\n')
        user_input = input('Press enter to continue or type q to quit\n')
    times.close()


def genScramble(n):
    moves = ['R', 'M', 'U', 'L', 'D']
    movelist = []
    s = len(moves)
    last = Move()
    move = Move()
    for _ in range(n):
        while not move.checkGood(last):
            i = random.randrange(s)
            move = Move(moves[i])
            m = random.randrange(3)
            if m == 1:
                move.setMod("'")
            if m == 2:
                move.setMod('2')
        last = move
        movelist.append(move)
    print(' '.join(str(m) for m in movelist))


start()