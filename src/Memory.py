import queue
import itertools
import threading
import Process
class MainMemory:
    mainMemory = 512 # MB
    usedMemory = 0 # MB
    frameSize = 32 / 1000 # MB aka 32 KB
    tableSize = 35
    q = queue.Queue()
    def __init__(self):
        self.frameTable = [None] * self.tableSize
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
    virtualMemory = 512 # MB aka 2^29 logical address space
    usedMemory = 0 # MB
    pageSize = 32 / 1000 # MB or 32 KB
    pageNumIter = itertools.count()
    def __init__(self):
        self.logicalMemory = []
        self.disk = []
    def getMemoryLeft(self):
        return self.virtualMemory - self.usedMemory
    def useMemory(self, used):
        lock = threading.Lock()
        with lock:
            if (self.usedMemory + used > self.virtualMemory):
                raise ValueError('Used memory cannot exceed virtual memory!')
            else:
                self.usedMemory = self.usedMemory + used
                print(f'Virtual memory remaining: {self.getMemoryLeft()} MB')

    def addPages(self, process): #Upon Process creation, pages for each Process operation are added to logical memory in order to move to ready state
        if (len(self.logicalMemory) < (self.virtualMemory / self.pageSize)):
            opList = process.operationsList
            count = 0
            for op in opList:
                self.logicalMemory.append((process.id, next(self.pageNumIter))) # references page number
                self.useMemory(self.pageSize)
        #print(self.logicalMemory)
        self.toPageTable(process)
    def toPageTable(self, process):
        count = 0
        for page in self.logicalMemory:
            if (page[0] == process.id):
                pageNum = page[1]
                offset = count # for now offset def aults to 0
                #count += 1
                process.pageTable.append((pageNum, offset))
        #print(process.pageTable)
    def toPhysical(self, process, frameTable):
        lock = threading.Lock()
        with lock:
            for page in process.pageTable:
                index = page[0] + page[1]
                if (len(frameTable) > index and frameTable[index] == None and frameTable.count(None) > 0):
                    frameTable[index] = f'Page {page[0]}'
                elif (len(frameTable) > index and frameTable.count(None) > 0):
                    emptyIndex = frameTable.index(None)
                    pageIndex = process.pageTable.index(page[0])
                    frameTable[emptyIndex] =  f'Page {page[0]}'
                    process.pageTable[pageIndex] =  (page[0], emptyIndex-page[1])
                else: # Basic page replacement algorithm
                    newIndex = 0 # Victim selection (first frame) - essentially a FIFO queue because processes arrive at same time in order
                    #print(process.pageTable)
                    count = 0
                    pageIndex = -1
                    for element in page:
                        if (element == page[0]):
                            index = count
                        count += 1
                    victim = frameTable[newIndex]
                    self.disk.append(victim)
                    frameTable[newIndex] = f'Page {page[0]}'
                    process.pageTable[pageIndex] = (page[0], page[1]*-1)
                #print (frameTable)
