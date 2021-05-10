import random

def bubble_sort(arr):
    for s in range(0,len(arr)-1):
        finished = True
        for i in range(0,len(arr)-1-s):
            if arr[i] > arr[i+1]:
                ##Flag to detect if sort is already finished
                finished = False
                ##Swap items
                arr[i],arr[i+1] = arr[i+1],arr[i]
        print(arr)
        if finished:
            return arr
    return arr

def run():
    arr = []
    for _ in range(20):
        arr.append(random.randint(1,25))
    arr = [25,34,98,7,41,19,5,17,11,12]
    print(bubble_sort(arr))