#!/usr/bin/env python3
'''
Python 7 mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot klasi, kura pārveido 5. nodarbības mājasdarbu Nr. 2 saturu par klasi

'''
import matplotlib.pyplot as plt
import json


class TopWords:
    '''
    Izveidot klasi, kurai ir 2 publiskas metodes:
    - setVardnica -  definē failu
    - grafiks - izvada grafiku

    Klasei nav pieejami publiski parametri
    '''
    def setVardnica(self, vardnicaFails):
        file = open(vardnicaFails)
        self.__vardnica = json.load(file)
        file.close()

    def grafiks(self):
        # izsaucot šo metodi izvada bar tipa grafiku. dati ir parametrs __vardnica
        # TODO  

        vardi = list(self.__vardnica.keys())
        biezs = list(self.__vardnica.values())

        fig, ax = plt.subplots()

        ax.bar(vardi, biezs)
        ax.set_xlabel('Vārdi')
        ax.set_ylabel('Biežums')
        
        plt.show()      


if __name__ == "__main__":
    obj = TopWords()
    obj.setVardnica("top_vardi.json")
    
    obj.grafiks()
