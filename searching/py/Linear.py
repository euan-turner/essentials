import random
def linear_search(items,val):
    for i in range(len(items)):
        if items[i] == val:
            return i
    return None

def enum_linear_search(size,item):
    arr = []
    for i in range(size):
        arr.append(random.randint(1,100))
    indices = []
    arr = enumerate(arr)
    for i in arr:
        if i[1] == item:
            indices.append(i[0])
    return indices

print(enum_linear_search(100,7))








items = ['New York', 'Washington','Florida','Arizona','Nevada','Texas','California','Alaska','Maine']
print(linear_search(items,'Texas'))
print(linear_search(items,'Hawaii'))