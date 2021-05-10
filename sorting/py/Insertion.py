import random

def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr = arr[i] ##Current item
        insert = i ##Index to insert current item before
        for j in range(0,i): ##Item to compare to, previous to current
            if curr < arr[j]:
                insert = j
                break
        arr.pop(i)
        
        arr = arr[:insert] + [curr] + arr[insert:]
    return arr



def run():
    arr = []
    for _ in range(20):
        arr.append(random.randint(1,20))


    print(arr)
    print(insertion_sort(arr))


