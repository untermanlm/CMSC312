import multiprocessing
import sys
from datetime import time
from time import sleep

from SeedGenerator import readProgramFile, createProcess
import Process
import psutil
import tkinter as tk
import subprocess as sub
validOperations = ['CALCULATE', 'I/O', 'FORK']
# def update():
#     text = tk.Text(root)
#     curr_process = multiprocessing.current_process()
#     curr_process.data
#     #str1 = 'ID: ' + str(curr_process.id) + ' STATE: ' + curr_process.state + '\n'
#     text.insert(tk.INSERT, str1)
#     text.pack()
#     root.after(1000, update)
def callback(*args):
    global processList
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
        except ValueError:
            print('Invalid number of processes.')
    if(msg == 'START'):
        print(processList)
        print(processes)
        for p in processes:
            p.start()
        for p in processes:
            p.state = 'EXIT'
            p.join()
    if (msg == 'STATS'):
        print('Printing stats!')
        for p in processes:
            print(f'ID: {p.id}, State: {p.state}, Schedule Type: {p.scheduleType}')
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
                #p.state = 'EXIT'
                p.join(0.08 * numCycles)
                if p.is_alive():
                    p.terminate()
                    p.join()

        except ValueError:
            print('Invalid number of cycles.')
    if(msg == 'CLEAR'):
        print('Clearing processes')
        processList.clear()
        processes.clear()


def main():
    print()
if __name__ == "__main__":
    # stdoutOrigin = sys.stdout
    # sys.stdout = open('processLog.txt', 'w')
    instructions = []
    processList = []
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


