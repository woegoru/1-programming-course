def binary_search(value, array):
    num = 0
    num2 = len(array)-1
    while num <= num2:
        mid = (num + num2)//2
        if value > array[mid]:
           num = mid + 1
        elif array[mid] > value:
            num2 = mid - 1
        elif value == array[mid]:
            return mid
    return -1
        
