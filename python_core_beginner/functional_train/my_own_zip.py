def zip_(list1: list, list2: list)-> tuple:
    x = len(list1)
    result = []
    result1 = []
    if len(list2) < x:
        x = len(list2)
    for element in range(x):
        result_list = result1.copy()
        result_list.append(list1[element])
        result_list.append(list2[element])
        result_list = tuple(result_list)
        result.append(result_list)
    return result

list1 = [1, 5, 3, 8, 35]
list2 = [2, 7, 9]
print(zip_(list1, list2))
