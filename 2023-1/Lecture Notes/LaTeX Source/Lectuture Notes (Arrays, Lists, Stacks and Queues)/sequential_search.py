def sequential_search(lst, element):
    """
    Search for the given element in the list using sequential search.
    """
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1