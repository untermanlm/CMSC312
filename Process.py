import sys
from multiprocessing import Process
import Operations
import itertools
class P(Process):
    id_iter = itertools.count()
    def __init__(self):
        super(P, self).__init__()
        self.id = next(self.id_iter)
        self._state = 'NEW'
        self._operationsList = []
        self._scheduleType = 'FCFS'

    @property
    def operationsList(self):
        return self._operationsList
    @operationsList.setter
    def operationsList(self, o):
        self._operationsList = o
        self._state = 'READY'

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
    def run(self):
        newID = str(self.id)
        logName = 'processLog' + newID + '.txt'
        sys.stdout = open(logName, 'w')
        if (self._scheduleType == 'FCFS'):
            Operations.firstComeFirstServe(self)
        if (self._scheduleType == 'SJF'):
            Operations.shortestJobFirst(self)
        sys.stdout.close()