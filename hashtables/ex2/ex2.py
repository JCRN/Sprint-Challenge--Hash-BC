#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Put tickets into ht
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)
        
    # Construct the route
    key = 'NONE'
    
    for i in range(length):
        val = hash_table_retrieve(hashtable, key)
        key = val
        route[i] = val
        
    return route
