def linear_search(items,val):
    for i in range(len(items)):
        if items[i] == val:
            return i
    return None







items = ['New York', 'Washington','Florida','Arizona','Nevada','Texas','California','Alaska','Maine']
print(linear_search(items,'Texas'))
print(linear_search(items,'Hawaii'))