def insertionSort(Array):
    for step in range(1, len(Array)):
        key = Array[step]
        i = step-1
        print("key", key, "i", Array[i])
        while (i >= 0 and key < Array[i]):
            Array[i+1] = Array[i]
            i -= 1

        Array[i+1] = key
    return Array


Array = [9, 5, 1, 4, 3]
print(insertionSort(Array))
