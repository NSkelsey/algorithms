# Select uses the median of medians approach to narrow down the number of elements we
# are considering. It narrows the search space down by n/13 - n/5 or
# something....
# The recurrence is T(n) = T(2n/10) + T(7n/10) when the list is of length 5

G = [19, 9, 301, 2, 4, 5,
     12, 23, 7, 6, 200,
     43, 22, 96, 100, 8,
     101, 102, 109, 110,
     201, 50, 43, 35, 21,
     88, 31, 250, 100, 16]


def select(A, i): # A is a list, i is the ith element in that ordered list
                  # NOTE all elements must be unique
    T = list(A)
    if len(A) <= 5: # Base case, just find ith element
        T = list(A)
        T.sort()
        return T[i]
    p = median_of_medians(A)
    (A_l, A_r, i_p) = partition(A, p)
    if i_p == i:
        return p
    elif i_p < i:
        return select(A_r, i - i_p - 1)    
    else: # i_p > i
        return select(A_l, i)
    
def median_of_medians(A):
    B = list()                # B will hold medians of sublists
    itrs, i = len(A)/5, 0
    for j in range(itrs): # divide list into sublists of len 5
        sub_list = A[i:i+5]  
        m = median(sub_list)
        B.append(m)
        i += 5
    end = len(A) % 5 
    if end != 0:
        B.append(median(A[-end:])) # add the last group to the pot
    p = select(B, len(B)/2)
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
    i = len(T)/2 #  in list of 4 selects the 3rd element
    return T[int(i)]
    
def proof(A, i): # naive impl of select to justify correctness
    A = list(A)
    A.sort()
    print A[i]

if __name__ == "__main__":
    import sys
    from random import shuffle, randint
    if len(sys.argv) != 3:
        print "Usage: python select.py <position> <Array size>"
        exit(1)
    x = int(sys.argv[1])
    r = randint(1,100)
    G = range(r,r+int(sys.argv[2]))
    shuffle(G)
    print "The array before selection:\n", G, "\nThe %dth element of the sorted list:"%x
    proof(G, x)
    print '='*20, "My solution", '='*20
    print(select(G, x))



