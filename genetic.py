import time

def genetic(array_of_processors, end_time):
    length = len(array_of_processors)
    start_time = time.clock()

    while True:
        #Podejmujemy prb krzyowania.
        for index in range(0, length-1):
            #Sortujemy procesory po sumie czasow.
            array_of_processors = sorted(array_of_processors, key=sum)

            mniejszy = array_of_processors[index]
            wiekszy = array_of_processors[length-1]

            #print(sum(mniejszy), sum(wiekszy))  #Test. Do wykasowania

            #Koczymy pr krzyowania, jeli udao si krzyowanie dowonych dwch osobnikw.
            #Wane! Pominicie tego kroku mo skutkowa pogorszeniem wyniku.
            sukces = krzyzowanieWszystkieIndeksy(mniejszy, wiekszy)
            if sukces:
                break

        #Wyj z funkcji jli przekroczono limit czasu
        if time.clock() - start_time > end_time:
            print(time.clock() - start_time)
            return array_of_processors

    return array_of_processors


#Ponij ne wersje funkcji do krzyowania.
def balance (mniejszy, wiekszy):
    difference = sum(mniejszy) - sum(wiekszy)
    #Jeli rnica czasu pomidzy procesami jest rwna 0, nie naey nic zminia
    if(difference == 0):
        return False
    #Rnica czasu wykona(podzielona przez 2)
    diff = int(difference/2)
    #Minimalna rica mliwa do uzyskania po poprawieniu
    abs_diff =10000

    # zauwazylem ze elementy o tych samych indeksach czesto maja dosc ciekawe roznice pomiedzy wartosciami i ta petla porownuje je poszukujac
    #najblizszej optimum pary do zamiany, jest tak przez to ze my je sortujemy w greedym

    to_change =0
    for i in range(min(len(mniejszy), len(wiekszy))):
        if abs(mniejszy[i]-wiekszy[i] - diff)< abs_diff:
            to_change = i
            abs_diff = abs((mniejszy[i] - wiekszy[i]) - diff)

    #Zracamy faz, jei nie uda si poprawi osobnika.
    if abs(diff) <= abs(abs_diff):
        return False

    #Krzyujemu osobniki jeli poprawi to wynik
    temp1 = mniejszy[to_change]
    temp2 = wiekszy[to_change]

    mniejszy[to_change] = temp2
    wiekszy[to_change] = temp1

    #Zwracamy true jeli udao s poprawi osobnika
    return True

def krzyzowanieWszystkieIndeksy(mniejszy, wiekszy):
    difference = sum(mniejszy) - sum(wiekszy)
    #Jeli rnica czasu pomidzy procesami jest rowna 0, nie naezy nic zminia
    if(difference == 0):
        return False
    #Roznica czasu wykonan(podzielona przez 2)
    diff = int(difference/2)
    #Minimalna roznica mozliwa do uzyskania po poprawieniu
    abs_diff =10000

    # zauwazylem ze elementy o tych samych indeksach czesto maja dosc ciekawe roznice pomiedzy wartosciami i ta petla porownuje je poszukujac
    #najblizszej optimum pary do zamiany, jest tak przez to ze my je sortujemy w greedym

    to_change = 0
    for i in range(len(mniejszy)):
        for j in range(len(wiekszy)):
            if abs(mniejszy[i]-wiekszy[j] - diff)< abs_diff:
                to_change = {'mniejszy':i, 'wiekszy':j}
                abs_diff = abs((mniejszy[i] - wiekszy[j]) - diff)

    #Zracamy fazsz, jeli nie uda si poprawi osobnika.
    if abs(diff) <= abs(abs_diff):
        return False

    #Krzyzujemu osobniki jeli poprawi to wynik
    temp1 = mniejszy[to_change['mniejszy']]
    temp2 = wiekszy[to_change['wiekszy']]

    mniejszy[to_change['mniejszy']] = temp2
    wiekszy[to_change['wiekszy']] = temp1

    #Zwracamy true jeli udazo  poprawi osobnika
    return True
