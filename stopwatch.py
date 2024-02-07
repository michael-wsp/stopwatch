import time
import math

class SolveTime:
    def __init__(self, t):
        self.min = math.floor(t / 60)
        self.sec = math.floor(t % 60)
        self.ms = math.floor((t % 1) * 1000)
    def __repr__(self):
        return f'{self.min}m {self.sec}s {self.ms}ms'


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
    times = open('times.txt', 'w')
    while user_input != 'q':
        t = stop_watch()
        times.write(f'{t}\n')
        user_input = input('Press enter to continue or type q to quit\n')
    times.close()

start()