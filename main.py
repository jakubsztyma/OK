import generator, greedy

if __name__ == "__main__":
    # Set variables.
    processorsNumber = 100
    processCount = 5000
    maxLength = 100
    fileName = "instance"


    #Create instance and write to file.
    #It is provided, that the optimal solution is equal to sum(proc) / processorsNumber
    generator.createInstanceToFile(fileName, processorsNumber, processCount, maxLength)

    #Read instance from file
    procLength = generator.readInstanceFromFile(fileName, processCount)
    optimumResult = sum(procLength) // processorsNumber

    #Execute greedy algorithm.
    greedyResult = greedy.greedy(processorsNumber, processCount, procLength)

    #Compare results.
    print(optimumResult)
    print(greedyResult)