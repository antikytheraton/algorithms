import random

random.seed(42)
# List to order
num_list = [i for i in range(10)]
random.shuffle(num_list)
# print(num_list)


def bubble_sort(shuffle_list):
    '''
    A simple exchange sort algorithm that works by
    repeatedly stepping through the list to be
    sorted, comparing each pair of adjacent items
    and swapping them if they are in the wrong
    order. The pass through the list is repeated
    until no swaps are needed.
    Parameters
    - shuffle_list: list of integer numbers
    '''
    assert isinstance(shuffle_list, list)
    alist = shuffle_list
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

sorted_list = bubble_sort(num_list)
# print(sorted_list)