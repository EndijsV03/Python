#!/usr/bin/env python3
import datu_generators
import math
import matplotlib.pyplot as plt
import numpy as np

'''
Python   projekts Nr.1.2
Uzdevums: aizpildīt vietas ar atzīmi TODO
Problēma: datu_generators.py ģenerē datus ar lineāru tendenci.
          Ar lineāro regresiju und vienkāršu optimizāciju ir nepieciešams
          atrast vienādojumu, ar kuru var paredzēt y vērtības pie sekojošiem x:
                x1 = 999
                x2 = -673
                x3 = 777
Mērķis: atrast optimālāko vienādojumu, lai assert komandas būtu veiksmīgas

Noteikumi!!! 
    - visa kalkulācija notiek ar bibliotēku numpy
    - Assert komandas nedrīkst izmest kļūdu

Papildus Info:
    https://en.wikipedia.org/wiki/Linear_regression
    Lineārā regresija definē vienādojumu, kas paskaidro lineāru tendenci:
        y = A*x + B
        Lineārās regresijas uzdevums ir atras vispiemēratāko:
            Slīpumu - A
            Novirzi - B
'''

## Importēt ģenerētos datus
# šie ir ievades dati, ar kuriem būs jāstrāda
# tie tiek dinamiski ģenerēti
x_all,y_all,testi=datu_generators.generet_datus()

## Papildfunkcijas, lai apskatītu datus
# tikai ievades datus
def grafiks_input(x_all,y_all):
    plt.scatter(x_all,y_all)
    plt.show()
# ievades datus un linēāro līkni
def grafiks(x_all,y_all,x,y):
    # ievades dati
    plt.scatter(x_all,y_all)
    # līkne
    plt.scatter(x,y,color='red',linewidth=2)
    plt.show()

#### Uzdevumi sākas šeit ####
## 1. vizualizēt ievades datus un iegūt iespaidu par tiem
# TODO: vizualizēt ievades datus ar papildfunkciju
grafiks_input(x_all, y_all)

## 2. Iegūt iespaidu, kā strādā lineārā regresija
# TODO: definē sevis izvēlētus parametrus A un B
A_savs = 2 # TODO: izvēlies savu vērtību
B_savs = 69 # TODO: izvēlies savu vērtību

def kalk_liniju(A,B,x_all):
    # TODO: izveidot funkciju
    '''
    Funkcija:
        - izveido vektoru pēc vienādojuma:
            y = A*x + B
        - vektora garums tiek definēts no x_all vektora
            maksimālā un minimālā x_all vērtības
        - vektora punktu daudzums tiek definēts:
            no minimālās līdz maksīmālai x_all vērtībai ar soli 1
    Ievade: 
        A - Slīpuma koeficients
        B - Novirzes koificients
        x_all - x ass vektors no ģenerētiem datiem
    Izvade: 
        x - lineāras regresijas x ass vektors
        y - lineāras regresijas y ass vektors
    '''
    # Iegūst minimālo un maksimālo x_all vērtību
    x_min = np.min(x_all)
    x_max = np.max(x_all)
    
    # Izveidojam x vektoru no minimālās līdz maksimālajai vērtībai ar soli 1
    x = np.arange(x_min, x_max, 1)
    
    # Izveidojam y vektoru, izmantojot lineāro vienādojumu
    y = A * x + B

    x = np.array([])
    y = np.array([])

    # TODO: atkomentēt assert, kas pārbauda vai vektors ir pareiza garuma
    #assert testi["len"]==len(x)
    return x,y

x,y = kalk_liniju(A_savs, B_savs, x_all)
# TODO: vizualizēt ievades datus un izveidoto līniju ar papildfunkciju
grafiks(x_all,y_all,x,y)
# TODO: Kāds novērojums?

## 3. Izrēķināt atšķirību starp izveidoto līniju un ievades datiem.

def kalk_atskiribu(x,y,x_all,y_all):
    # TODO: izveidot funkciju
    '''
    Funkcija:
        - piemeklē katram x_all un y_all punktam tuvāko x,y punktu, 
            Ideja ir parādīta "Tuvakais_punkts.PNG" Failā
        - aprēķina mazāko distanci katram tuvākam punktam
        - aprēķina vidējo vērtību no visu punktu minimālām distancēm
    Tips:
        - Distanci var aprēķināt ar sekojošām metodēm:
            - Eiklīda metode https://en.wikipedia.org/wiki/Euclidean_distance
            - Manhetenas metode https://en.wikipedia.org/wiki/Taxicab_geometry
            - Un citas - Hamming Metode ...
    Ievade: 
        x,y - Lineārās regresijas vektors
        x_all,y_all - ievades datu vektors
    Izvade: 
        kluda_avg - vidējā aprēķinātā kļūda starp izveidoto un ģenerēto vektoru
        
    '''
    def eiklida_attalums(x1, y1, x2, y2):
        return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    kludas = []

    for i in range(len(x_all)):
        min_attalums = math.inf 

        for j in range(len(x)):
            attalums = eiklida_attalums(x_all[i], y_all[i], x[j], y[j])

            if attalums < min_attalums:
                min_attalums = attalums

        kludas.append(min_attalums)

    kluda_avg = np.mean(kludas)
    return kluda_avg

kluda = kalk_atskiribu(x,y,x_all,y_all)

## 4. Mainīt A un B konstanti tā, lai tiktu atrast mazākā kļūda jeb atšķirība
#grafiks_input(x_all,y_all)

# TODO: variēt A un B sevis izvēlētā diapazonā un atrast tās vērtības, ar kurām ir 
#       mazākā kļūda. Šīs vērtības vislabāk paskaidro lineāro tendenci.
# TIPS: Šo uzdevumu var dažādi atrisināt:
#           - pragmātiski, pārbaudīt katru rezultātu diapazonā
#           - Gradient descent metodi vai citu optimizācijas algoritmu



# TODO: Novērot iznākumu ar atrastām vērtībām A_fit un B_fit
#x,y=kalk_liniju(A_fit,B_fit,x_all)
grafiks(x_all,y_all,x,y)

## 5. pārbaudīt iznākumu
# TODO: atkomentēt assert komandas, lai pārbaudītu rezultātu
#assert (abs(A_fit*999+B_fit) >= abs(testi["x1"][0])) and (abs(A_fit*999+B_fit) <= abs(testi["x1"][1]))
#assert (abs(A_fit*(-673)+B_fit) >= abs(testi["x2"][0])) and (abs(A_fit*(-673)+B_fit) <= abs(testi["x2"][1]))
#assert (abs(A_fit*777+B_fit) >= abs(testi["x3"][0])) and (abs(A_fit*777+B_fit) <= abs(testi["x3"][1]))
