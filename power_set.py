from itertools import combinations

def power_set(A):
    """Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.
    Returns:
        (list(sets)): The power set of A as a list of sets.
    """

    i = 0
    n = len(A)
    my_list = []
    while i < (n+1):
        my_list = my_list + list(combinations(A,i))
        i += 1
    return [set(i) for i in my_list]
