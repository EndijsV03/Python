import random

###########################
########### setup
###########################
n = 7
s = set(range(1, n))
l = [random.randint(1, n-1) for x in range(n)]
print(l)

###########################
########### atrodi dubultos
###########################
# Use Floyd's Tortoise and Hare algorithm to find duplicates
def find_duplicates(nums):
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]

        if tortoise == hare:
            break
        
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    
    return ptr1

print(find_duplicates(l))

