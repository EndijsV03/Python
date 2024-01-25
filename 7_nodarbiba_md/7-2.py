#!/usr/bin/env python3
'''
Python 7 mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

'''

from IntroOpenCV import IntroOpenCV
from TopWords import TopWords

class Majasdarbs(TopWords, IntroOpenCV):
    pass


if __name__ == "__main__":
    obj = Majasdarbs()

    # Atkomentēt sekojošās rindas, lai pārbaudītu vai klases ir mantotas
    # TODO
    obj.set_picture("python.jpg")
    obj.get_black_white()
    obj.setVardnica("top_vardi.json")
    obj.grafiks()
