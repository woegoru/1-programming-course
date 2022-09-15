def linear_search(value, array):
    for i in range(len(array)):
        if array[i] == value:
            return(i)
    
    return(-1)
        
