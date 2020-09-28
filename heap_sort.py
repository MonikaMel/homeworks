a = [10, 5, 3, 15, 41, 51, 74, 1, 55, 456, 221, 556,  9, 12, 7, 5, 17, 2]

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


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


print(heap_sort(a))
