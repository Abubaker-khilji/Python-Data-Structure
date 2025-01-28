def monotonic_array(array):
    n = len(array)
    if n==0: return True
    first = array[0]
    last = [n-1]
    if first>last:
        #monotonic decrease or array is not monotonic
        for k in range(n-1):
            if array[k]< array[k+1]: return False
    elif first == last:
        #monotonic - all value are equal 
        for k in range(n-1):
            if array[k]!= array[k+1]:return False

    else:
        #first < last
        # monotonic increase or not monotonic 
        for k in range (n-1):
            if array[k] > array[k+1]:return False

    return True                      