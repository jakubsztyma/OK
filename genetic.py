import time

def genetic(array_of_processors, end_time):
    length = len(array_of_processors)
    start_time = time.clock()

    while True:
        #Podejmujemy próbę krzyżowania.
        for index in range(0, length-1):
            #Sortujemy procesory po sumie czasow.
            array_of_processors = sorted(array_of_processors, key=sum)

            mniejszy = array_of_processors[index]
            wiekszy = array_of_processors[length-1]

            #print(sum(mniejszy), sum(wiekszy))  #Test. Do wykasowania

            #Kończymy próbę krzyżowania, jeśli udało się krzyżowanie dowonych dwóch osobników.
            #Ważne! Pominięcie tego kroku może skutkować pogorszeniem wyniku.
            sukces = krzyzowanieWszystkieIndeksy(mniejszy, wiekszy)
            if sukces:
                break

        #Wyjdź z funkcji jeśli przekroczono limit czasu
        if time.clock() - start_time > end_time:
            print(time.clock() - start_time)
            return array_of_processors

    return array_of_processors


#Poniżej różne wersje funkcji do krzyżowania.
def balance (mniejszy, wiekszy):
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

    to_change =0
    for i in range(min(len(mniejszy), len(wiekszy))):
        if abs(mniejszy[i]-wiekszy[i] - diff)< abs_diff:
            to_change = i
            abs_diff = abs((mniejszy[i] - wiekszy[i]) - diff)

    #Zracamy fałsz, jeśli nie uda się poprawić osobnika.
    if abs(diff) <= abs(abs_diff):
        return False

    #Krzyżujemu osobniki jeśli poprawi to wynik
    temp1 = mniejszy[to_change]
    temp2 = wiekszy[to_change]

    mniejszy[to_change] = temp2
    wiekszy[to_change] = temp1

    #Zwracamy true jeśli udało się poprawić osobnika
    return True

def krzyzowanieWszystkieIndeksy(mniejszy, wiekszy):
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
