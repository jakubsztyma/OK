#Grupa 1.1

import generator, greedy, genetic
import math

if __name__ == "__main__":
    # Set variables.
    processorsNumber = 100
    processCount = 5000
    maxLength = 100

    fileName = "instance"

    #read_name = "instancje/m50n1000.txt"
    #read_name = "instancje/instance"
    #read_name = "instancje/testKolejnosc.txt"
    read_name = "instancje/m25.txt"
    #read_name = "instancje/2_1000_25_3.txt"


    #Create instance and write to file.
    #It is provided, that the optimal solution is equal to sum(proc) / processorsNumber
    generator.createInstanceToFile(fileName, processorsNumber, processCount, maxLength)

    #Read instance from file


    # latwiejsze wczytywanie z obcego pliku


    file = open(read_name, 'r')
    processorsNumber = int (file.readline())
    processCount = int (file.readline())
    file.close()

    procLength = generator.readInstanceFromFile(read_name, processCount)
    optimumResult = math.ceil(sum(procLength) / processorsNumber)

    #Execute greedy algorithm.
    array_of_processors = []
    array_of_processors = greedy.greedy(processorsNumber, processCount, procLength)
    array_of_processors = sorted(array_of_processors,)
    sum_array = []

    for i in range (processorsNumber):
        sum_array.append(sum(array_of_processors[i]))
    greedyResult = max(sum_array)



    #Compare results.

    print ("\noptimum result")
    print(optimumResult )
    print ("\ngreedy result")
    print(greedyResult)

    # execute genetic algorithm
    array_after_genetic = []
    sum_array= []
    array_after_genetic = genetic.genetic(array_of_processors, 2)  #Drugi parametr to ilość sekund.

    for i in range(processorsNumber):
        sum_array.append(sum(array_after_genetic[i]))
    print( "wynik po genetycznym")
    print (max(sum_array))

    for i in range(len(array_after_genetic)):
        print(sorted(array_after_genetic[i], reverse=True), sum(array_after_genetic[i]))



