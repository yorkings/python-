def bubbleSort(array):
    count = 0
    for i in range(len(array)):
        count = count + i
        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp




bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)
