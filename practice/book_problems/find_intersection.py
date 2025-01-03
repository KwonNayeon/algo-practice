# Filename: find_intersection.py

# Method 1: Using list comprehension
def return_inter(list1, list2):
    list3 = [v for v in list1 if v in list2]
    return list3

# Method 2: Using set intersection
def return_inter_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

# Test data
list1 = [7, 12, 15, 24, 33, 42]  # 이번주 복권번호
list2 = [1, 12, 17, 24, 33, 45, 62, 32, 11]  # 자주 나타난 번호들

# Test both methods
print(return_inter(list1, list2))
new_list = return_inter_set(list1, list2)
print(new_list)