arr = ["B", "E", "K", "J", "A", "U", "P"]
data = "J"

def get_ascii_value(arr):
    l = [ord(i) for i in arr]
    return l

def binary_search(seq, elem):
    array = get_ascii_value(seq)
    item = ord(elem)
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = start + (end - start) // 2
        middle_value = array[middle]
        if middle_value == item:
            return middle # or return chr(int(middle_value))
        elif middle_value > item:
            end = middle - 1
        else:
            start = middle + 1
    return None


print(binary_search(arr, data))