#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.1

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''
import numpy as np

# izveidot numpy random 3x3 matricu
print("Random: \n")
arr = np.random.rand(3,3)
print(arr)
print('\n')

# izveidot citu numpy matricu, kas ir inversā matrica no pirmās matricas
print("Inversa: \n")
arr_inv = np.linalg.inv(arr) 
print(arr)
print('\n')

# sareizināt abas matricas un noapaļot līdz integer precizitātei
print("Reizinajums: \n")
reizinājums = np.rint(np.dot(arr, arr_inv))
print(reizinājums)

# Izveidot trešo matricu, kas ir 3x3 identitātes matrica 
identitates_matrica = np.eye(3) # TODO

# Pārbaudīt vai identitates_matrica ir vienāda ar reizinājumu!
vienads = bool(np.array_equal(identitates_matrica, reizinājums))

# Lai pārbaudītu iznākumu, atkomentēt nākamo rindu
assert vienads == True