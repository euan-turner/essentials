import random
##Recursive merge sort - sorts in place
def recursive_merge(arr):
    print("Splitting: ", arr)
    if len(arr) > 1:
        m = len(arr)//2
        left = arr[:m]
        right = arr[m:]

        recursive_merge(left)
        recursive_merge(right)

        ##Merge subarrays
        i = j = k = 0
        ##i,j are indices for left,right
        ##k is the index to change arr at 
        print("Merging: ", arr)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        ##Place remaining items from left or right
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

##Iterative merge sort
def iterative_merge(arr):
    ##Split arr into list of single-item lists
    for i in range(len(arr)):
        arr[i] = [arr[i]]
    
    while len(arr) != 1:
        index = 0
        ##Merge pairs
        while index < len(arr) - 1:
            new = merge(arr[index], arr[index+1])
            arr[index] = new
            del arr[index+1]
            index += 1
    return arr[0]

##Merge two sub-arrays for iterative_merge
def merge(left,right):
    new = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            new.append(left[l])
            l += 1
        else:
            new.append(right[r])
            r += 1

    ##Place remaining items
    if l < len(left):
        new += left
    elif r < len(right):
        new += right
    return new


def run():
    arr = []
    for _ in range(20):
        arr.append(random.randint(1,20))
    print(iterative_merge(arr.copy()))
    recursive_merge(arr)
    print(arr)



