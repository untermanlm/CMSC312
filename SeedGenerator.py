import random

def readProgramFile(fileName, validOperations):
    instructions = []
    with open(fileName) as f:
        for line in f:
            if (any(ele in line for ele in validOperations)):
                line = line.strip()
                instructions.append(line)
    return instructions

def createProcess(instructions):
    processList = []
    for instruction in instructions:
        arr = instruction.split(' ')

        #come back later to make more systematic instead of programmed in
        operation = arr[0]
        minCycle = int(arr[1])
        maxCycle = int(arr[2])
        randNum = random.randint(minCycle, maxCycle)

        processList.append((operation, randNum))
    return processList