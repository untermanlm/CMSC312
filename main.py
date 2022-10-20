from SeedGenerator import readProgramFile, createProcess
from Operations import calculate, io, fork
def fcfs(processList):
    for operation in processList:
        arr = operation.split(' ')
        operator = arr[0]
        cycles = int(arr[1])
        if (operator == 'CALCULATE'):
            calculate(cycles)
        elif (operator == 'I/O'):
            io(cycles)
        elif (operator == 'FORK'):
            fork(cycles)
        else:
            print("Unknown operator")

def main():
    fileName = "programfile1.txt"
    validOperations = ['CALCULATE', 'I/O', 'FORK']
    instructions = readProgramFile(fileName, validOperations)
    processList = createProcess(instructions)
    fcfs(processList)
    print(processList)


if __name__ == "__main__":
    main()
