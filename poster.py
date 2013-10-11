# placement computes the maximal sum of elements of V
# where V_i is constrained by the position specified by X_i
# and a distance D between other elements
def placement(X, V, D):
    B = [0 for x in range(len(X))] # Our algorithim uses a greedy approach that
                                   # runs in O(n) and memoimizes previous solns in B
    d_i = 0                        # the chasing pointer
    S = [[0]]                       # the solution matrix
    for i in range(len(X)):        # Big outer loop (n operations) 
        # compute prev max
        prev_max = 0 
        ctr = d_i
        step = 0
        while D <= (X[i] - X[ctr]):     # inner loop (never does more than D iterations)
            if prev_max <= B[ctr]:      # prev_max + current V[i] is our new max
                prev_max = B[ctr]
                step = ctr
            ctr += 1                    # loops from d_i upto D <= X[i] - X[ctr] 
        if (X[i] - X[d_i]) > D:
            d_i += 1
        B[i] = prev_max + V[i]          # build out B[i]     
        S.append(list(S[step]) + [i])   # builds the solution matrix if needed

    # output formatting after this point
    soln, _max = 0, 0
    for j in range(len(B) - D, len(B)):
        if _max < B[j]: soln = S[j + 1]; _max = B[j]
    print B, S
    return  _max, soln              # must use max of last D to find real answer


if __name__ == "__main__":
    X = [1, 2, 5, 6, 9, 15, 17]
    V = [2, 3, 2, 10, 12, 1, 4]
    D = 4
    #X = range(1, 20)
    #V = range(1, 20)
    X_V = [(X[i], V[i]) for i in range(len(X))]
    print "Given the list of x_i, v_i tuples:\n", X_V, "\nand distance: %d between each x_i" % D
    print "The optimal V sum is: %d and the selection is the  %s indexed positions" %  placement(X, V, D)

