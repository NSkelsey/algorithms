#include <stdlib.h>
#include <stdio.h>

// computes a^n in O(log n) multiplications
// no negatives and nothing that overflows please
int power(int a, int n) {
    int r = 1;
    for (n; ffs(n) > 0; n = n >> 1) { // ffs finds first set bit, returns 0 if none
        if (n % 2 == 1) {
            r = r*a;
        }
        a = a*a;
    }
    return r;
}

int  main (int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <int> <int>\n", argv[0]);
        exit(0);
    }
    int a = atoi(argv[1]);
    int n = atoi(argv[2]);
    printf("%d^%d = %d\n", a, n, power(a, n));
}
