import time

def genetic( array_of_processors, end_time):


     #start = time.clock()
    #sortowanie wzgledem czasu wykonywanie na danym procesorze malejaco

    for i in range (200):
        for i in range (len(array_of_processors)):

            array_of_processors[i].insert(0,sum(array_of_processors[i]))

        array_of_processors.sort()
        array_of_processors.reverse()
        for i in range(len(array_of_processors)):
            array_of_processors[i].pop(0)

        X1 = array_of_processors[0]
        length = len(array_of_processors)
        X2=  array_of_processors[length-1]

        X = []
        X = balance(X1, X2)

    return array_of_processors



def balance (X1, X2):

    diff = int((sum(X1) - (sum(X2)))/2)
    abs_diff =100

    # zauwazylem ze elementy o tych samych indeksach czesto maja dosc ciekawe roznice pomiedzy wartosciami i ta petla porownuje je poszukujac
    #najblizszej optimum pary do zamiany, jest tak przez to ze my je sortujemy w greedym

    to_change =0
    for i in range(min(len(X1), len(X2))):
        if ((abs ((X1[i]-X2[i]) - diff ))< abs_diff):
            to_change = i
            abs_diff =(abs ((X1[i]-X2[i]) - diff ))



    temp1= X1[to_change]
    temp2 = X2[to_change]

    X1.remove(temp1)
    X2.remove(temp2)
    X1.append(temp2)
    X2.append(temp1)
    X2.sort()
    X2.reverse()
    X1.sort()
    X1.reverse()
    X = []
    X.append(X1)
    X.append(X2)
    return X


















