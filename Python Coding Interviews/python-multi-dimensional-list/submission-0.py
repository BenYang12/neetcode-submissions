from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    res = []
    for sublist in nested_arr:
        max_in_sublist = float('-inf')
        for elem in sublist:
            max_in_sublist = max(max_in_sublist, elem)
        res.append(max_in_sublist)
    return res
    


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
