# Select uses the median of median approach to narrow down the number of elements we
# are considering. It narrows the search space down by n/13 - n/5 or
# something....
# The recurrence is T(n) = T(2n/10) + T(7n/10) when the list is of length 5

G = [19, 9, 301, 2, 4, 5,
     12, 23, 7, 6, 200,
     43, 22, 96, 100, 8,
     101, 102, 109, 110,
     201, 50, 43, 35, 21,
     88, 31, 250, 100, 16]


def select(A, i, d=1): # A is a list, i is the ith element in that ordered list
                  # NOTE all elements must be unique
    T = list(A); T.sort()
    print "select on: ", d*'\t',i, T
    if len(A) <= 5: # Base case, just find ith element
        T = list(A)
        T.sort()
        return T[i]
    p = medianOfMedians(A, d)
    (A_l, A_r, i_p) = partition(A, p)
    if i_p == i:
        return p
    elif i_p < i:
        return select(A_r, i - i_p - 1, d+1)    
    else: # i_p > i
        return select(A_l, i, d+1)
    
def medianOfMedians(A,d):
    B = list()                # B will hold medians of sublists
    itrs, i = len(A)/5, 0
    for j in range(itrs): # divide list into sublists of len 5
        sub_list = A[i:i+5]  
        m = median(sub_list)
        B.append(m)
        i += 5
    end = len(A) % 5 
    if end != 0:
        B.append(median(A[-end:]))
    print "MoM of \t",d*'\t', B
    p = select(B, len(B)/2, d+1)
    print "MoM is \t",d*'\t', p
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
    return A_l, A_r, i_p


def median(A):  # A cheat to find the median in our base case
    T = list(A) # copies list!
    T.sort()
    if len(A) % 2 == 0:
        print "even list"
    i = len(T)/2 #  in list of 4 selects the 3rd element
    return T[int(i)]
    
def proof(A, i): # naive impl of select to justify correctness
    A = list(A)
    A.sort()
    print A
    print A[i]

if __name__ == "__main__":
    import sys
    from random import shuffle
    #A = [3, 4, 9, 1, 2]
    x = int(sys.argv[1])
    G = range(200)
    shuffle(G)
    proof(G, x)
    print '='*20, "My solution", '='*20
    print(select(G, x, 1))
    B = [1, 2, 3, 4, 5, 6]
    #proof(B, 5)



