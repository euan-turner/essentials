##Calculate hash value for items
def calc_hash(item, size):
    ascii_sum = sum([ord(i) for i in item])
    return ascii_sum % size

##Create a hash table for a list of hashed value
def create_table(items, size):
    print("Creating table")
    table = ['' for _ in range(size)]

    ##Place data in table
    for item in items:
        hash_val = calc_hash(item,size)
        while table[hash_val-1] != '':
            hash_val += 1
        table[hash_val-1] = item
    return table

def hash_search(item, table):
    found = False
    index = calc_hash(item, len(table))
    ##Check if item exists in table
    if table[index-1] != '':
        while not found and index<len(table):
            if table[index-1] == item:
                found = True
            else:
                index +=1 
    return index-1 if found else None
            

    

items = ['Florida','Georgia','Delaware','Alabama','California','North Dakota','New York']
table_size = 14
hash_table = create_table(items, table_size)
print(hash_table)
flor_index = hash_search('Florida',hash_table)
err_check = hash_search('Nevada',hash_table)
print(flor_index,err_check)
