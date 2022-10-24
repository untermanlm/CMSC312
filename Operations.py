import random
import time
import multiprocessing


def shortestJobFirst(process):
    operationList = process.operationsList
    sorted_1 = sorted(operationList, key=lambda x: x[1])
    for operation in sorted_1:
        operator = operation[0]
        cycles = operation[1]
        if (operator == 'CALCULATE'):
            process._state = 'RUN'
            print(process.state)
            calculate(cycles)
        elif (operator == 'I/O'):
            process._state = 'WAIT'
            print(process.state)
            io(cycles)
        elif (operator == 'FORK'):
            print()
        else:
            print("Unknown operator")
def firstComeFirstServe(process):
    operationList = process.operationsList
    for operation in operationList:
        operator = operation[0]
        cycles = operation[1]
        if (operator == 'CALCULATE'):
            process._state = 'RUN'
            print(process.state)
            calculate(cycles)
        elif (operator == 'I/O'):
            process._state = 'WAIT'
            print(process.state)
            io(cycles)
        elif (operator == 'FORK'):
            print()
        else:
            print("Unknown operator")
def calculate(numCycles):
    lock = multiprocessing.Lock()
    temp = numCycles
    calculation = 0
    while(numCycles > 0):
        with lock:
            numCycles -= 1
            calculation += 1 #arbitrary calculation
            time.sleep(0.05)
            print(f"Calculating: {numCycles} / {temp} cycles remaining.\n")
    print()
def io(numCycles):
    lock = multiprocessing.Lock()
    temp = numCycles
    while (numCycles > 0):
        with lock:
            numCycles -= 1
            time.sleep(0.05)
            print(f"Waiting: {numCycles} / {temp} cycles remaining.\n")
    print()

#to be developed
def fork():
    print()