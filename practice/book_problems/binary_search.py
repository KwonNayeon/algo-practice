# Traditional binary search implementation
def binary_search(a_list, n):
    """Binary search implementation - O(log n)"""
    first = 0
    last = len(a_list) - 1
    
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        elif n < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


# Using Python's bisect module
from bisect import bisect_left

def binary_search_bisect(an_iterable, target):
    """Binary search using bisect_left - O(log n)"""
    index = bisect_left(an_iterable, target)
    if index < len(an_iterable) and an_iterable[index] == target:
        return True
    return False
