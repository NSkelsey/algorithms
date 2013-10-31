# A polynomial time algorithm that greedily finds an order to complete homework
# assignments so that the maximium lateness of any submitted homework is
# minizimized. Runs in O(n^2logn)
import heapq

# INPUT:
# A list of tuples where each tuple represents a single assignment a
# Each tuple contains (d, t) where d reprsents the time when a is due
# t represents the time it takes to complete the assignment

# OUTPUT:
# The order in which the assignments should be completed


def minimize_lateness(A):
    cur_time = 0
    lateness_arr = []
    while len(lateness_arr) > 0 or cur_time == 0: # runs n times
        lateness_arr = []
        for i in range(len(A)):
            d, t = A[i]
            l_i = (cur_time + t) - d # how late the assignment will be
            lateness_arr.append((-l_i, i)) # -l_i because we are using a min heap
        heapq.heapify(lateness_arr) # nlogn operations
        l_i, i = heapq.heappop(lateness_arr)
        a = A[i] # a is the lastest assignment
        cur_time += A[i][1] # we spent time t on this assignment
        A.remove(a)
        print a, cur_time

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 1:
        print "Usage: python homework.py"
        exit(1)
    A = [(20, 10), (4, 3), (2, 4), (3, 6), (16, 3), (19, 1)]
    minimize_lateness(A)
