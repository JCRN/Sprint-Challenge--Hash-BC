#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Insert given weights into ht
    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)
    
    # Get the idxs: use the difference of (limit - weight) to find a 2nd idx
    for i, weight in enumerate(weights):
        i2 = hash_table_retrieve(ht, (limit-weight))
        if i2 is not None:
            return (i2, i) if (i2 > i) else (i, i2)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
