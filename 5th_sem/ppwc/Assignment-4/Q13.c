#include <stdio.h>

int main() {
    int m = 10, n = 5;
    int *mp, *np;
    
    mp = &m;  // mp points to m
    np = &n;  // np points to n
    
    *mp = *mp + *np;  // m = m + n --> m = 10 + 5 --> m = 15
    *np = *mp - *np;  // n = m - n --> n = 15 - 5 --> n = 10
    
    printf("%d %d\n%d %d\n", m, *mp, n, *np);  // Print m, *mp, n, *np
    return 0;
}
