def binary_search(lst,val):
    found = False
    start = 0
    end = len(lst)-1
    while start <= end and not found:
        mid = (start+end)//2
        
        if lst[mid] == val:
            found = True
        elif lst[mid] > val:
            end = mid-1
        elif lst[mid] < val:
            start = mid+1
        

    
    return mid if found else None


a = [1,2,3,4,5,6,7,8,9,10]
b = binary_search(a,7)
print(b)