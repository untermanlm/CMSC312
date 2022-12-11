import threading
from SeedGenerator import readProgramFile, createProcess
import Process
import tkinter as tk
import itertools
validOperations = ['CALCULATE', 'I/O', 'FORK']
def update():
    stats = ''
    for p in processes:
        if (p.runtime > 0):
            stat = 'ID: ' + str(p.id) + ' STATE: ' + p.state + ' RUNTIME: ' + str(p.runtime) + ' seconds' + '\n'
        else:
            stat = 'ID: ' + str(p.id) + ' STATE: ' + p.state + '\n'
        stats += stat
    valuesLabel.configure(text=stats)
    root.after(1000, update)
def callback(*args):
    global operationsList
    global instructions
    global multi
    msg = e.get()
    if ('LOAD' in msg):
        try:
            print("Loading operations")
            fileName = msg[5:]
            f = open(fileName, 'r')
            instructions = readProgramFile(fileName, validOperations)
        except OSError:
            print("Not a valid file")
    if ('SETPROC' in msg):
        try:
            numProcesses = int(msg[8:])
            print(f'Initializing {numProcesses} processes.')
            for i in range(0, numProcesses):
                if (len(instructions) > 0):
                    processList = createProcess(instructions)
                p = Process.P()
                if (len(processList) > 0):
                    p.operationsList = processList
                if (i == numProcesses - 1):
                    p.scheduleType = 'SJF'
                processes.append(p)
                operationsList.append(processList)
        except ValueError:
            print('Invalid number of processes.')
        except UnboundLocalError:
            print('Need to load processes first!')
    if(msg == 'START'):
        print(operationsList)
        print(processes)
        for p in processes:
            if (p.state == 'READY'):
                p.start()
            else:
                while(Process.m1.getMemoryLeft() < p.memoryreq):
                    p.wait()
                Process.m1.useMemory(p.memoryreq, p)
                Process.m2.addPages(p)
                Process.m2.toPhysical(p, Process.m1.frameTable)
                p.start()
        for p in processes:
            p.join()
    if (msg == 'MULTI'):
        if (len(processes) % 2 == 0):
            multi = True
            cpu0 = []
            cpu1 = []
            for p in processes:
                if (p.processor == 0):
                    cpu0.append(p)
                else:
                    cpu1.append(p)
            for (a,b) in itertools.zip_longest(cpu0, cpu1):
                if (a.state == 'READY' and b.state == 'READY'):
                    print(f'CPU 0 starting Process {a.id}')
                    a.start()
                    print(f'CPU 1 starting Process {b.id}')
                    b.start()
                else:
                    if(Process.m1.getMemoryLeft() < a.memoryreq):
                        while(Process.m1.getMemoryLeft() < a.memoryreq):
                            a.wait()
                        Process.m1.useMemory(a.memoryreq, a)
                        Process.m2.addPages(a)
                        Process.m2.toPhysical(a, Process.m1.frameTable)
                        a.start()
                    if (Process.m1.getMemoryLeft() < b.memoryreq):
                        while(Process.m1.getMemoryLeft() < b.memoryreq):
                            b.wait()
                        Process.m1.useMemory(b.memoryreq, b)
                        Process.m2.addPages(b)
                        Process.m2.toPhysical(b, Process.m1.frameTable)
                        b.start()
            for (a,b) in itertools.zip_longest(cpu0, cpu1):
                a.join()
                b.join()
        else:
            print('MULTI LIMITATION: NUM PROCESS MUST BE EVEN')

    if (msg == 'STATS'):
        print('Printing stats!')
        if (multi == False):
            for p in processes:
                if (p.runtime > 0):
                    print(f'Thread ID: {p.id}, State: {p.state}, Runtime: {p.runtime} seconds, Schedule Type: {p.scheduleType}, Memory Requirement: {p.memoryreq} MB')
                else:
                    print(f'Thread ID: {p.id}, State: {p.state}, Schedule Type: {p.scheduleType}, Memory Requirement: {p.memoryreq} MB')
        else:
            for p in processes:
                if (p.runtime > 0):
                    print(f'CPU: {p.processor}, Thread ID: {p.id}, State: {p.state}, Runtime: {p.runtime} seconds, Schedule Type: {p.scheduleType}, Memory Requirement: {p.memoryreq} MB')
                else:
                    print(f'CPU: {p.processor}, Thread ID: {p.id}, State: {p.state}, Schedule Type: {p.scheduleType}, Memory Requirement: {p.memoryreq} MB')

        #print("Individual log files will be stored as processLog(id).txt")
        # sys.stdout.close()
        # sys.stdout = stdoutOrigin
    if('SUSPEND' in msg):
        try:
            numCycles = int(msg[8:])
            print(f'Suspending processes after {numCycles} cycles.')
            for p in processes:
                p.start()
            for p in processes:
                p.stop = True
                p.join(0.08 * numCycles)
                if p.is_alive():
                    p.join()
        except ValueError:
            print('Invalid number of cycles.')
    if(msg == 'CLEAR'):
        print('Clearing processes')
        operationsList.clear()
        processes.clear()
def main():
    print()
if __name__ == "__main__":
    instructions = []
    operationsList = []
    processes = []
    multi = False

    root = tk.Tk()
    root.geometry('400x400')

    L = tk.Label(text='Input commands here (look at documentation for command guide):')
    L.pack()

    e = tk.Entry(root)
    e.pack()
    e.bind("<Return>", callback)

    pLabel = tk.Label(text='Processes:')
    pLabel.pack()

    valuesLabel = tk.Label(text='')
    valuesLabel.pack()

    update()
    root.mainloop()
