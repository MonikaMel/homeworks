arr = ["B", "E", "K", "J", "A", "U", "P"]
data = "A"


def heap_sort(a):
    for i in range(1, len(a), 1):
        j = i
        while j > 0 and a[j] > a[(j - 1) // 2]:
            a[j], a[(j - 1) // 2] = a[(j - 1) // 2], a[j]
            j = (j - 1) // 2

    for k in range(0, len(a) - 1, 1):
        a[0], a[len(a) - 1 - k] = a[len(a) - 1 - k], a[0]
        n = 0
        while 2 * n + 1 < len(a) - 1 - k:
            maximum = n
            if a[maximum] < a[2 * n + 1]:
                maximum = 2 * n + 1
            if 2 * n + 2 < len(a) - 1 - k and a[maximum] < a[2 * n + 2]:
                maximum = 2 * n + 2
            if maximum == n:
                break
            else:
                a[maximum], a[n] = a[n], a[maximum]
            n = maximum
    return a


def get_sorted_ascii_value(arr):
    l = [ord(i) for i in arr]
    return heap_sort(l)


def binary_search(seq, elem):
    array = get_sorted_ascii_value(seq)
    item = ord(elem)
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = start + (end - start) // 2
        middle_value = array[middle]
        if middle_value == item:
            return seq.index(chr(int(middle_value)))  # or return chr(int(middle_value))
        elif middle_value > item:
            end = middle - 1
        else:
            start = middle + 1
    return None


print(binary_search(arr, data))