import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        p1 = 1
        p2 = len(arr) -1
        
        while p2 >= p1:

            while p1 <= p2 and arr[p1] <= pivot:
                p1 += 1

            while p2 >= p1 and arr[p2] >= pivot:
                p2 -= 1
            
            if p2 > p1:
                arr[p1],arr[p2] = arr[p2],arr[p1]
        
        ##Swap pivot and p2
        arr[0],arr[p2] = arr[p2],arr[0]

        left = quicksort(arr[:p2])
        right = quicksort(arr[p2+1:])

        return left + [arr[p2]] + right

arr = []
for _ in range(20):
    arr.append(random.randint(1,20))
print(arr)
print(quicksort(arr))