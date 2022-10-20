import time
from multiprocessing import Process, Lock, Value
def calculate(numCycles):
    for i in range(numCycles):
        time.sleep(0.05)
def io(numCycles):
    print()
def fork():
    print()
if __name__ == '__main__':
    total = Value('i', 500)
    lock = Lock()
