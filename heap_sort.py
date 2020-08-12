# Complexity 👇
a = [10, 5, 3, 15, 9, 12, 7, 5, 17, 2]


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

# Complexity

# Since our tree height is O(lg(n)),
# we could do up to O(lg(n)) moves.
# Across all n nodes, that's an overall time complexity of O(nlg(n)).
# After transforming the tree into a heap,
# we remove all n elements from it—one item at a time.
# Removing from a heap takes O(lg(n)) time,
# since we have to move a new value to the root of the heap and bubble down.
# Doing n remove operations will be O(nlg(n)) time.
