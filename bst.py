def binary_search_leftmost (SA, num, L, R):
    while L < R:
        m = (L + R) // 2
        if SA[m] < num:
            L = m+1
        else:
            R = m
    return L if SA[L] == num else -1

def binary_search_rightmost (SA, num, L, R):
    while L < R:
        m = ( L + R ) // 2
        if SA[m] > num:
            R = m
        else:
            L = m+1
    return R-1 if SA[R-1] == num else -1

def search (SA, num):
    end = len(SA) - 1
    lpos = binary_search_leftmost  (seq, num, 0, end)
    if lpos == -1:
        print(f'Searched element {num} not found')
    else:
        rpos = binary_search_rightmost (seq, num, 0, end)
        print(f'Searched element {num} found in the array-index range : {lpos+1} to {rpos+1} ')
    
seq = [1, 1, 1, 2, 2, 4, 4, 4, 4, 5, 5, 8, 8, 8, 10, 11, 11, 11, 11, 11]
num = int(input("Enter search number : "))
search (seq, num)
