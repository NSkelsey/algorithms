algorithms
==========

Implementations of various algorithms in various languages. Enjoy


power.c
-------
Computes a^n in O(logn) operations.

example:

```bash
./a.out 4 12
```


select.py
---------
Selects the kth ordered element in an unordered list in O(n) time.

Example usage:
```
python select.py 87 100
```

Which outputs:
```
The array before selection:
[5, 14, 2, 55, 38, 33, 96, 83, 66, 15, 21, 70, 30, 67, 94, 92, 64, 78, 80, 45,
79, 99, 71, 24, 1, 27, 75, 72, 16, 35, 49, 6, 12, 52, 17, 53, 81, 87, 73, 7, 3,
58, 61, 88, 77, 51, 95, 40, 37, 4, 82, 29, 41, 42, 63, 13, 43, 32, 98, 10, 93,
69, 34, 91, 31, 86, 22, 18, 23, 19, 36, 50, 60, 25, 97, 44, 76, 8, 0, 85, 57,
39, 26, 46, 68, 56, 28, 20, 48, 89, 62, 74, 84, 9, 54, 65, 11, 59, 47, 90] 
The 87th element of the sorted list:
87
==================== My solution ====================
87
```

homework.py
-----------
Greedy algorithm that demonstrates that you can minimize the maximum lateness of
all of your homework by picking the assignment that will be the latest right
now.

Example usage:
```
python homework.py
```

Which outputs:
```
(3, 6) 6
(2, 4) 10
(4, 3) 13
(20, 10) 23
(16, 3) 26
(19, 1) 27
```
