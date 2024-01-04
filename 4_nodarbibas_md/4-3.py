#!/usr/bin/env python3
'''
Python mājasdarbs Nr.4-3

Uzdevums: aizpildīt vietas ar atzīmi TODO
Apraksts: Šīs programmas uzdevums ir lejupielādēt grāmatu 
          un veik dažādas darbības ar tās saturu
'''

import urllib.request
import os
import string
import sys
#import helperMajasdarbs

#####################
## Funkcijas
#####################

def url_to_filename(url):
    """
        Funkcija paņem kādu URL sadala to ar atdalītāju / un izvedo faila nosaukumu
        Ievade: URL
        Izvade: Faila nosaukums

    """
    *tmp, part1, part2 = url.split( "/" )    
    print( tmp, part1, part2 )
    if len(part1) > 0:
        filename = part1 + "_" + part2
    else:
        filename = part2
    return filename

def get_text(url):
    """
    Funkcija izveido faila nosaukumu un lejupielāde failu, ja tāds neeksistē.
    Ievade: URL
    Izvade: Faila saturs
    """
    # Faila nosaukumu no grāmatas url konstruēt
    filename = url_to_filename(url)

    # Ja fails vēl nav nolādēts, tad lejupielādēt
    if not os.path.isfile(filename):
        print("downloading...")
        urllib.request.urlretrieve(url, filename)

    # Atvērt failu ar utf-8 encoding un izvadīt faila saturu
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        return text

def replace_non_ascii_by_space(text):
    """
    Funkcija aizstāj visas Ne ASCII simbolus ar atstarpi
    Ievade: teksts
    Izvade: Pārveidots teksts
    """
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

#####################
## Globāli parametri
#####################

# Saraksts ar iespējamām grāmatām
gramatas = ["https://gutenberg.org/files/834/834-0.txt",
            "https://gutenberg.org/files/66351/66351-0.txt",
            "https://gutenberg.org/files/108/108-0.txt"]

# Atdalāmie simboli, kas atdala vārdus
strip = string.whitespace + string.punctuation + string.digits + "\"'" + " "

#####################
## Šeit sākas maģija
#####################

## Izmantojot funkciju get_text, dabūt saturu no grāmatas kas atrodama files sarakstā otrā rindā
selected_book = gramatas[1]
text = get_text(selected_book)

## tekstu pārveidot tā, lai visi burti būtu ar mazo burtu (lowercase)
text = text.lower()

## izsaukt funkciju replace_non_ascii_by_space un padot tai parametru text
text = replace_non_ascii_by_space(text)

# Tukša vārdnīca, kur tiks saglabāts katrs vārds ar tā biežumu
words = {}

# Tekstu pa vārdiem sadalīt un saglabāt izveidotajā vārdnīcā
for word in text.split():

    # no vārda atdalīt simbolu
    word = word.strip(strip)

    # saglabāt tikai vārdus, kuri garāki par 2 simboliem
    if len(word) > 2:
        # palielināt vārda skaitu vārdnīcā par 1
        words[word] = words.get(word, 0) + 1

## Izveidot listi ar 100 biežāk lietotiem vārdiem

sorted_list = sorted(words.items(), key=lambda x: x[1], reverse=True)

top_vardi = [word for word, _ in sorted_list[:100]]

print("top 100 no vienas grāmatas")
print(top_vardi)


##  Izveido vārdnīcu "words", kas satur visu 3 grāmatu vārdus 
# (līdzīgi kā ar vienu grāmatu augšā, bet jāiterē cauri grāmatām)

# Tukša vārdnīca, kur tiks saglabāts katrs vārds ar tā biežumu
words = {}

# Izmantojot funkciju get_text, dabūt saturu no visām grāmatām
for selected_book in gramatas:
    text = get_text(selected_book)

    # Tekstu pārveidot tā, lai visi burti būtu ar mazo burtu (lowercase)
    text = text.lower()

    # Izsaukt funkciju replace_non_ascii_by_space un padot tai parametru text
    text = replace_non_ascii_by_space(text)

    # Tekstu pa vārdiem sadalīt un saglabāt izveidotajā vārdnīcā
    for word in text.split():
        # No vārda atdalīt simbolus
        word = word.strip(strip)

        # Saglabāt tikai vārdus, kuri garāki par 2 simboliem
        if len(word) > 2:
            # Palielināt vārda skaitu vārdnīcā par 1
            words[word] = words.get(word, 0) + 1

## Kādi top 100 no visām 3 grāmatām?
sorted_list = sorted(words.items(), key=lambda x: x[1], reverse=True)
top_vardi = [word for word, _ in sorted_list[:100]]

print("\ntop 100 no visām 3 grāmatas")
print(top_vardi)

# TODO