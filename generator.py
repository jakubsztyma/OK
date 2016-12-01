from random import randint

#Function does not guarantee th proper number of processes and optimum.
def createInstanceToFile(fileName, processorsNumber, processCount, maxLength):
    width = (processorsNumber * maxLength) // 4

    #Generate processes.
    processes = generate(fileName, processorsNumber, processCount, maxLength, width)
    #Reduce the number of processes to fit thee processCount variable
    reduce(processes, maxLength, processCount)

    """ test
    for i in range(len(processes)):
        print(len(processes[i]),sum(processes[i]), width)
    print(sum([len(row) for row in processes]))
    """
    #Write to file
    procLength = []
    for row in processes:
        procLength.extend(row)
    procLength = sorted(procLength)
    writeToFile(fileName, processorsNumber, processCount, procLength)

def writeToFile(fileName, processorNumber, processCount, procLength):
    file = open(fileName, 'w')
    file.write(str(processorNumber) + '\n')
    file.write(str(processCount) + '\n')
    for i in range(len(procLength)):
        file.write(str(procLength[i]) + '\n')

def reduce(processes, maxLength, processCount):
    current = sum([len(row) for row in processes])
    i = 0
    while current!= processCount:
        first, second = randint(0, len(processes[i])-1), randint(0, len(processes[i])-1)
        if first != second:
            length = processes[i][first] + processes[i][second]
            if length < maxLength:
                processes[i][first] = length
                processes[i].remove(processes[i][second])
                i += 1
                current -= 1
        if i == len(processes):
            i = 0

def generate(fileName, processorsNumber, processCount, maxLength, width):
    procLength = []

    #Generate processes
    for i in range(processorsNumber):
        proc = []
        usedLength = 0

        #Create for this processor.
        new = randint(1, maxLength//2)
        while usedLength + new <= width:
            proc.append(new)
            usedLength += new
            new = randint(1, maxLength//2)
        #Append the rest of free space
        if width - usedLength > 0:
            proc.append(width - usedLength)
        procLength.append(proc)

    return procLength


def readInstanceFromFile(fileName, processCount):
    file = open(fileName, 'r')
    #Skip unncesary data
    file.readline()
    file.readline()

    #Read times of processes
    procLength = []
    for i in range(processCount):
        procLength.append(int(file.readline()))
    return procLength