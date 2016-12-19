import time


def genetic(array_of_processors, end_time):
    length = len(array_of_processors)
    start_time = time.clock()

    while True:
        #Podejmujemy próbę krzyżowania jeden na jeden.
        sukces = False
        for index in range(0, length-1):
            #Sortujemy procesory po sumie czasow.
            array_of_processors = sorted(array_of_processors, key=sum)

            mniejszy = array_of_processors[index]
            wiekszy = array_of_processors[length-1]

            #Kończymy próbę krzyżowania, jeśli udało się krzyżowanie dowonych dwóch osobników.
            #Ważne! Pominięcie tego kroku może skutkować pogorszeniem wyniku.
            sukces = krzyzowanieJedenIJeden(mniejszy, wiekszy)
            if sukces:
                break

            # Wyjdź z funkcji jeśli przekroczono limit czasu
            if time.clock() - start_time > end_time:
                print(time.clock() - start_time)
                return array_of_processors

        if not sukces:
            #Jeśi nie udało się krzyżowanie jeden na jeden, próbujemy dwa na jeden
            for index in range(0, length - 1):
                # Sortujemy procesory po sumie czasow.
                array_of_processors = sorted(array_of_processors, key=sum)

                mniejszy = array_of_processors[index]
                wiekszy = array_of_processors[length - 1]

                # Kończymy próbę krzyżowania, jeśli udało się krzyżowanie dowonych dwóch osobników.
                # Ważne! Pominięcie tego kroku może skutkować pogorszeniem wyniku.
                sukces = krzyzowanieDwaIJeden(mniejszy, wiekszy)
                if sukces:
                    break
                sukces = krzyzowanieDwaIJeden(wiekszy, mniejszy)
                if sukces:
                    break

                #Wyjdź z funkcji jeśli przekroczono limit czasu
                if time.clock() - start_time > end_time:
                    print(time.clock() - start_time)
                    return array_of_processors

        if not sukces:
            #Jeśli nie udały się poprzednie krzyżowania, próbujmy dwa na dwa
            for index in range(0, length - 1):
                # Sortujemy procesory po sumie czasow.
                array_of_processors = sorted(array_of_processors, key=sum)

                mniejszy = array_of_processors[index]
                wiekszy = array_of_processors[length - 1]

                # Kończymy próbę krzyżowania, jeśli udało się krzyżowanie dowonych dwóch osobników.
                # Ważne! Pominięcie tego kroku może skutkować pogorszeniem wyniku.
                sukces = krzyzowanieDwaIDwa(mniejszy, wiekszy)
                if sukces:
                    break

                # Wyjdź z funkcji jeśli przekroczono limit czasu
                if time.clock() - start_time > end_time:
                    print(time.clock() - start_time)
                    return array_of_processors

        if not sukces:
            #Jeśli nie udały się poprzednie krzyżowania, próbujmy trzy na jeden
            for index in range(0, length - 1):
                # Sortujemy procesory po sumie czasow.
                array_of_processors = sorted(array_of_processors, key=sum)

                mniejszy = array_of_processors[index]
                wiekszy = array_of_processors[length - 1]

                # Kończymy próbę krzyżowania, jeśli udało się krzyżowanie dowonych dwóch osobników.
                # Ważne! Pominięcie tego kroku może skutkować pogorszeniem wyniku.
                sukces = krzyzowanieTrzyIJeden(mniejszy, wiekszy)
                if sukces:
                    break
                sukces = krzyzowanieTrzyIJeden(wiekszy, mniejszy)
                if sukces:
                    break

                #Wyjdź z funkcji jeśli przekroczono limit czasu
                if time.clock() - start_time > end_time:
                    print(time.clock() - start_time)
                    return array_of_processors

    return array_of_processors


#Krzyżowanie i wymiana jednego procsu na jeden.
def krzyzowanieJedenIJeden(mniejszy, wiekszy):
    difference = sum(mniejszy) - sum(wiekszy)
    #Jeśli różnica czasu pomiędzy procesami jest równa 0, nie naeży nic zminiać
    if(difference == 0):
        return False
    #Różnica czasu wykonań(podzielona przez 2)
    diff = int(difference/2)
    #Minimalna różnica możliwa do uzyskania po poprawieniu
    abs_diff =10000

    # zauwazylem ze elementy o tych samych indeksach czesto maja dosc ciekawe roznice pomiedzy wartosciami i ta petla porownuje je poszukujac
    #najblizszej optimum pary do zamiany, jest tak przez to ze my je sortujemy w greedym

    to_change = 0
    for i in range(len(mniejszy)):
        for j in range(len(wiekszy)):
            if abs(mniejszy[i]-wiekszy[j] - diff)< abs_diff:
                to_change = {'mniejszy':i, 'wiekszy':j}
                abs_diff = abs((mniejszy[i] - wiekszy[j]) - diff)

    #Zracamy fałsz, jeśli nie uda się poprawić osobnika.
    if abs(diff) <= abs(abs_diff):
        return False

    #Krzyżujemu osobniki jeśli poprawi to wynik
    temp1 = mniejszy[to_change['mniejszy']]
    temp2 = wiekszy[to_change['wiekszy']]

    mniejszy[to_change['mniejszy']] = temp2
    wiekszy[to_change['wiekszy']] = temp1

    #Zwracamy true jeśli udało się poprawić osobnika
    return True

#Krzyżowanie i wymiana dóch procesów na 1.
def krzyzowanieDwaIJeden(mniejszy, wiekszy):
    difference = sum(mniejszy) - sum(wiekszy)
    #Jeśli różnica czasu pomiędzy procesami jest równa 0, nie naeży nic zminiać
    if(difference == 0):
        return False
    #Różnica czasu wykonań(podzielona przez 2)
    diff = int(difference/2)
    #Minimalna różnica możliwa do uzyskania po poprawieniu
    abs_diff =10000

    # zauwazylem ze elementy o tych samych indeksach czesto maja dosc ciekawe roznice pomiedzy wartosciami i ta petla porownuje je poszukujac
    #najblizszej optimum pary do zamiany, jest tak przez to ze my je sortujemy w greedym

    to_change = 0
    for i1 in range(len(mniejszy)):
        for i2 in range(len(mniejszy)):
            for j in range(len(wiekszy)):
                if i1!=i2:
                    if abs(mniejszy[i1]+mniejszy[i2]-wiekszy[j] - diff)< abs_diff:
                        to_change = {'mniejszyA':i1,'mniejszyB':i2, 'wiekszy':j}
                        abs_diff = abs((mniejszy[i1]+mniejszy[i2] - wiekszy[j]) - diff)

    #Zracamy fałsz, jeśli nie uda się poprawić osobnika.
    if abs(diff) <= abs(abs_diff):
        return False


    #Krzyżujemu osobniki jeśli poprawi to wynik
    temp1a = mniejszy[to_change['mniejszyA']]
    temp1b = mniejszy[to_change['mniejszyB']]
    temp2 = wiekszy[to_change['wiekszy']]

    mniejszy.remove(temp1a)
    mniejszy.remove(temp1b)
    wiekszy.remove(temp2)

    mniejszy.append(temp2)
    wiekszy.append(temp1a)
    wiekszy.append(temp1b)

    #Zwracamy true jeśli udało się poprawić osobnika
    return True

#Krzyżowanie i wymiana dwóch procesów na dwa.
def krzyzowanieDwaIDwa(mniejszy, wiekszy):
    difference = sum(mniejszy) - sum(wiekszy)
    #Jeśli różnica czasu pomiędzy procesami jest równa 0, nie naeży nic zminiać
    if(difference == 0):
        return False
    #Różnica czasu wykonań(podzielona przez 2)
    diff = int(difference/2)
    #Minimalna różnica możliwa do uzyskania po poprawieniu
    abs_diff =10000

    # zauwazylem ze elementy o tych samych indeksach czesto maja dosc ciekawe roznice pomiedzy wartosciami i ta petla porownuje je poszukujac
    #najblizszej optimum pary do zamiany, jest tak przez to ze my je sortujemy w greedym

    to_change = 0
    for i1 in range(len(mniejszy)):
        for i2 in range(len(mniejszy)):
            for j1 in range(len(wiekszy)):
                for j2 in range(len(wiekszy)):
                    if i1!=i2 and j1!=j2:
                        if abs(mniejszy[i1]+mniejszy[i2]-wiekszy[j1] -wiekszy[j2] - diff)< abs_diff:
                            to_change = {'mniejszyA':i1,'mniejszyB':i2, 'wiekszyA':j1, 'wiekszyB':j2}
                            abs_diff = abs((mniejszy[i1]+mniejszy[i2] - wiekszy[j1] - wiekszy[j2]) - diff)

    #Zracamy fałsz, jeśli nie uda się poprawić osobnika.
    if abs(diff) <= abs(abs_diff):
        return False

    #Krzyżujemu osobniki jeśli poprawi to wynik
    temp1a = mniejszy[to_change['mniejszyA']]
    temp1b = mniejszy[to_change['mniejszyB']]
    temp2a = wiekszy[to_change['wiekszyA']]
    temp2b = wiekszy[to_change['wiekszyB']]

    mniejszy.remove(temp1a)
    mniejszy.remove(temp1b)
    wiekszy.remove(temp2a)
    wiekszy.remove(temp2b)

    mniejszy.append(temp2a)
    mniejszy.append(temp2b)
    wiekszy.append(temp1a)
    wiekszy.append(temp1b)

    #Zwracamy true jeśli udało się poprawić osobnika
    return True


#Krzyżowanie i wymiana trzech procesów na jeden
def krzyzowanieTrzyIJeden(mniejszy, wiekszy):
    difference = sum(mniejszy) - sum(wiekszy)
    #Jeśli różnica czasu pomiędzy procesami jest równa 0, nie naeży nic zminiać
    if(difference == 0):
        return False
    #Różnica czasu wykonań(podzielona przez 2)
    diff = int(difference/2)
    #Minimalna różnica możliwa do uzyskania po poprawieniu
    abs_diff =10000

    # zauwazylem ze elementy o tych samych indeksach czesto maja dosc ciekawe roznice pomiedzy wartosciami i ta petla porownuje je poszukujac
    #najblizszej optimum pary do zamiany, jest tak przez to ze my je sortujemy w greedym

    to_change = 0
    for i1 in range(len(mniejszy)):
        for i2 in range(len(mniejszy)):
            for i3 in range(len(mniejszy)):
                for j in range(len(wiekszy)):
                    if i1!=i2 and i1!=i3 and i2!=i3:
                        if abs(mniejszy[i1] + mniejszy[i2] + mniejszy[i3] - wiekszy[j] - diff)< abs_diff:
                            to_change = {'mniejszyA':i1,'mniejszyB':i2,'mniejszyC':i3, 'wiekszy':j}
                            abs_diff = abs((mniejszy[i1] + mniejszy[i2]+ mniejszy[i3] - wiekszy[j]) - diff)

    #Zracamy fałsz, jeśli nie uda się poprawić osobnika.
    if abs(diff) <= abs(abs_diff):
        return False

    #Krzyżujemu osobniki jeśli poprawi to wynik
    temp1a = mniejszy[to_change['mniejszyA']]
    temp1b = mniejszy[to_change['mniejszyB']]
    temp1c = mniejszy[to_change['mniejszyC']]
    temp2 = wiekszy[to_change['wiekszy']]

    mniejszy.remove(temp1a)
    mniejszy.remove(temp1b)
    mniejszy.remove(temp1c)
    wiekszy.remove(temp2)

    mniejszy.append(temp2)
    wiekszy.append(temp1a)
    wiekszy.append(temp1b)
    wiekszy.append(temp1c)

    #Zwracamy true jeśli udało się poprawić osobnika
    return True
