from random import random
from threading import Thread
import Operations
import itertools
import time
import Memory
import random

m1 = Memory.MainMemory()
m2 = Memory.VirtualMemory()
class P(Thread):
    id_iter = itertools.count()
    def __init__(self):
        super(P, self).__init__()
        self.id = next(self.id_iter)
        self._state = 'NEW'
        print(f'Process {self.id}: {self._state}')
        self._operationsList = []
        self._scheduleType = 'FCFS'
        self.stop = False
        self.memoryreq = (2 * pow(2, random.randint(6,8))) / 1000 # MB
        self.pageTable = []

    @property
    def operationsList(self):
        return self._operationsList
    @operationsList.setter
    def operationsList(self, o):
        self._operationsList = o
        try:
            m1.useMemory(self.memoryreq, self)
            m2.addPages(self)
            m2.toPhysical(self, m1.frameTable)
            self._state = 'READY'
        except ValueError:
            m1.addToQueue(self)
        print(f'Process {self.id}: {self._state}')

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, s):
        processStates = ['NEW', 'READY', 'RUN', 'WAIT', 'EXIT']
        if (s not in processStates):
            raise ValueError("Invalid process state")
        self._state = s

    @property
    def scheduleType(self):
        return self._scheduleType

    @scheduleType.setter
    def scheduleType(self, s):
        schedulers = ['FCFS', 'SJF']
        if (s not in schedulers):
            raise ValueError("Invalid scheduler")
        self._scheduleType = s
    def wait(self):
        time.sleep(1)
    def run(self):
        newID = str(self.id)
        start = time.time()
        if (self._scheduleType == 'FCFS'):
            Operations.firstComeFirstServe(self)
        if (self._scheduleType == 'SJF'):
            Operations.shortestJobFirst(self)
        end = time.time()

        if (self.stop == False):
            self.state = 'EXIT'
            print(f'Process {self.id}: {self._state}')
            print(f'Process {newID} finished after {round(end - start, 2)} seconds!')
            m1.relieveMemory(self.memoryreq)
            print(m2.logicalMemory)

