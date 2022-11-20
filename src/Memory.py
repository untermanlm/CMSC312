import queue
import itertools
import threading
import Process
class MainMemory:
    mainMemory = 512 # MB
    usedMemory = 0 # MB
    pageSize = 32 / 1000 # MB aka 32 KB
    q = queue.Queue()
    def __init__(self):
        self.pageTable = []
        self.processes = []
    def getMemoryLeft(self):
        return self.mainMemory - self.usedMemory
    def useMemory(self, used, process):
        lock = threading.Lock()
        with lock:
            if (self.usedMemory + used > self.mainMemory):
                raise ValueError('Used memory cannot exceed main memory!')
            else:
                self.usedMemory = self.usedMemory + used
                self.processes.append(process)
                print(f'Main memory remaining: {self.getMemoryLeft()} MB')
    def relieveMemory(self, used):
        lock = threading.Lock()
        with lock:
            if (self.usedMemory - used < 0):
                raise ValueError('Cannot relieve more memory than was available!')
            else:
                self.usedMemory = self.usedMemory - used
                print(f'Main memory remaining: {self.getMemoryLeft()} MB')
    def addToQueue(self, process):
        self.q.put(process)
    def printQueue(self):
        print(self.q)

class VirtualMemory:
    virtualMemory = 512 # MB aka 2^29
    pageSize = 32 / 1000 # MB or 32 KB
    pageNumIter = itertools.count()
    def __init__(self):
        self.pageTable = []
    def addPages(self, process):
        if (len(self.pageTable) < (self.virtualMemory / self.pageSize)):
            opList = process.operationsList
            for op in opList:
                self.pageTable.append((f'Process {process.id}', f'Page {next(self.pageNumIter)}'))
        print(self.pageTable)
if __name__ == "__main__":

    m1 = MainMemory()
    m1.useMemory(10)
    m1.getMemoryLeft()
