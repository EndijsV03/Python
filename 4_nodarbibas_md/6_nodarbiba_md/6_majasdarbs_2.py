#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''
import matplotlib.pyplot as plt
import json
import numpy as np
import os

# Importēt failu "top_vardi.json" un saglabāt atslēgas kā listi ar nosaukumu "x"
# vērtības kā listi ar nosaukumu "y"
# TODO
x = [] 
y = []

file_path = os.path.join(os.path.dirname(__file__), 'top_vardi.json')

with open(file_path, 'r') as file:
    data = json.load(file)
    for key, value in data.items():
        x.append(key)
        y.append(value)

# izveidot stabiņveidu grafiku kas rāda vārdu biežumu (y ass), Vārdus uz x ass
# piemērs ir mājasdarbu failā
fig, ax = plt.subplots()

ax.bar(x, y)
# TODO
ax.set_xlabel('Vārdi')
ax.set_ylabel('Biežums')

plt.xticks(rotation=45, ha='right', fontsize=8)
plt.show()



