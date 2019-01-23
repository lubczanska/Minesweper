from timeit import default_timer as timer
import time

start = timer()


def czas (start):
    return int(timer() - start)


while True:
    print(czas(start))

