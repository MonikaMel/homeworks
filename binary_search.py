def binary_search(seq, elem):
    start = 0
    end = len(seq) - 1

    while start <= end:
        middle = start + (end - start) // 2
        middle_value = seq[middle]
        if middle_value == elem:
            return middle
        elif middle_value > elem:
            end = middle - 1
        else:
            start = middle + 1
    return None


seq = [2, 5, 6, 8, 9, 11, 13, 14, 15]
a = binary_search(seq, 15)
print(a)
