

def greedy(processorsNumber, processCount, procLength ):



    myArray=[]
    for  i in range (processorsNumber):
        myArray.append([])

#sortowanie malejaco czasow procesow
    procLength.sort()
    procLength.reverse()
    proc_array=[]
    timer =0


    # Tworzenie "tablicy procesorow"
    for i in range (processorsNumber):
        temp = procLength.pop(0)
        myArray[i].append(temp)
        proc_array.append(temp)
        processCount-=1




    while (processCount >0):
        for i in range (processorsNumber):
            proc_array[i] -=1
            if proc_array[i]== 0 :
                temp = procLength.pop(0)
                myArray[i].append(temp)
                proc_array[i] = (temp)
                processCount-=1
            if processCount== 0:
                break
        timer +=  1



    #nie wszystkie procesory pracuja, brak kolejnych procesow, szukamy najdluazszego obecnie dzialajacego procesu
    max =0
    for i in range (processorsNumber):
        if (proc_array[i] > max):
            max = proc_array[i]

    timer += max


    return myArray;