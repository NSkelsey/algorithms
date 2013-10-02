# Select uses the median of median approach to narrow down the number of elements we
# are considering. It narrows the search space down by n/13 - n/5 or
# something....
# The recurrence is T(n) = T(2n/10) + T(7n/10) when the list is of length 5

A = [19, 9, 301, 2, 4, 5,
     12, 23, 7, 6, 200,
     43, 22, 96, 100, 8,
     101, 102, 109, 110,
     201, 50, 43, 35, 21,
     88, 31, 250, 100, 16]


def select(A, i): # A is a list, i is the ith element in that ordered list
                  # NOTE all elements must be unique
    T = list(A); T.sort()
    print "select on: \t", i, T
    if len(A) <= 5: # Base case, just find ith element
        list(A).sort()
        return A[i]
    p = medianOfMedians(A)
    (A_l, A_r, i_p) = partition(A, p)
    if i_p == i:
        return p
    elif i_p < i:
        return select(A_r, i - i_p)    
    else: # i_p > i
        return select(A_l, i)
    
def medianOfMedians(A):
    if len(A) == 1: # base case
        return A
    B = list()                # B will hold medians of sublists
    itrs, i = len(A)/5, 0
    for j in range(itrs): # divide list into sublists of len 5
        sub_list = A[i:i+5]  
        m = median(sub_list)
        B.append(m)
        i += 5
    end = len(A) % 5 
    if end != 0:
        B += A[-end:]
    print "MoM of\t\t", B
    p = select(B, len(A)/10)
    print "MoM is\t\t", p
    return p

def partition(A, p): # splits the list into left and right half where
                     # everything less is in the left list
    (A_l, A_r, i_p) = [], [], 0
    for elem in A:
        if p > elem:
            A_l.append(elem)
        elif p < elem:
            A_r.append(elem)
    i_p = len(A_l)
    print "Partition on:\t", A_l, p, A_r
    return A_l, A_r, i_p


def median(A):  # A cheat to find the median in our base case
    A = list(A) # copies list!
    A.sort()
    if len(A) % 2 == 0:
        print "even list"
    i = len(A)/2 #  in list of 4 selects the 3rd element
    return A[int(i)]
    
def proof(A, i): # naive impl of select to justify correctness
    A = list(A)
    A.sort()
    print A
    print A[i]

if __name__ == "__main__":
    import sys
    #A = [3, 4, 9, 1, 2]
    x = int(sys.argv[1])
    proof(A, x)
    print '='*20, "My solution", '='*20
    print(select(A, x))
    B = [1, 2, 3, 4, 5, 6]
    #proof(B, 5)



