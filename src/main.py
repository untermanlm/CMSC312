import threading
from SeedGenerator import readProgramFile, createProcess
import Process
import tkinter as tk
validOperations = ['CALCULATE', 'I/O', 'FORK']
# def update():
#     text = tk.Text(root)
#     stats = []
#     for p in processes:
#         stat = 'ID: ' + str(p.id) + ' STATE: ' + p.state + '\n'
#         stats.append(stat)
#     for stat in stats:
#         text.insert(tk.INSERT, stat)
#         text.pack()
#     root.after(1000, update)
def callback(*args):
    global operationsList
    global instructions
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
    if (msg == 'STATS'):
        print('Printing stats!')
        for p in processes:
            print(f'ID: {p.id}, State: {p.state}, Schedule Type: {p.scheduleType}, Memory Requirement: {p.memoryreq} MB')
        print("Individual log files will be stored as processLog(id).txt")
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
    # stdoutOrigin = sys.stdout
    # sys.stdout = open('processLog.txt', 'w')
    instructions = []
    operationsList = []
    processes = []

    root = tk.Tk()
    root.geometry('400x400')

    L = tk.Label(text='Input commands here (look at documentation for command guide):')
    L.pack()

    e = tk.Entry(root)
    e.pack()
    e.bind("<Return>", callback)

    pLabel = tk.Label(text='Processes:')
    pLabel.pack()


    #update()
    root.mainloop()
