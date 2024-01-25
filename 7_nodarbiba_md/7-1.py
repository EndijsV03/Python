#!/usr/bin/env python3
'''
Python 7 mājasdarbs Nr.1

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot jaunu datu tipu, kurš paņem vārdisku un skaitlisku vērtību, un pēc tam spēj atdod numeriskas vērtības
Datu tips atļauj sekojošos ievadvērtības:
- "one", "two", "three", "four", "five"
'''

class JaunsDatuTips:

    def __init__(self, vertiba):
        atbilstosie_skaitli = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        
        if vertiba in atbilstosie_skaitli:
            self.vertiba = vertiba
            self.numerisks = atbilstosie_skaitli[vertiba]
        else:
            print(f"Kļūda: Neatļauta vērtība '{vertiba}'. Iestatīts uz noklusējuma vērtību.")
            self.vertiba = "one"
            self.numerisks = 1

    def get_int(self):
        return self.numerisks

    def get_float(self):
        return float(self.numerisks)

    def get_string(self):
        return self.vertiba

if __name__ == "__main__":
    x1 = JaunsDatuTips("one")
    x2 = JaunsDatuTips("two")
    x3 = JaunsDatuTips("three")
    x4 = JaunsDatuTips("four")
    x5 = JaunsDatuTips("five")

    assert x1.get_int() == 1
    assert x2.get_int() == 2
    assert x3.get_int() == 3
    assert x4.get_int() == 4
    assert x5.get_int() == 5

    assert x1.get_float() == 1.0
    assert x2.get_float() == 2.0
    assert x3.get_float() == 3.0
    assert x4.get_float() == 4.0
    assert x5.get_float() == 5.0

    assert x1.get_string() == "one"
    assert x2.get_string() == "two"
    assert x3.get_string() == "three"
    assert x4.get_string() == "four"
    assert x5.get_string() == "five"
