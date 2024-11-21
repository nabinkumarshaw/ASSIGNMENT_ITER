#include <stdio.h>

int main() {
    // Define the size of the arrays
    int n = 5;  // For example, 5 elements in each array

    // Declare arrays a, b, c, d, and sumarray
    int a[n], b[n], c[n], d[n], sumarray[n];

    // Declare pointers to the arrays
    int *p_a = a, *p_b = b, *p_c = c, *p_d = d, *p_sum = sumarray;

    // Scan the arrays using pointers
    printf("Enter elements for array a:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", p_a + i);  // Accessing array a through pointer
    }

    printf("Enter elements for array b:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", p_b + i);  // Accessing array b through pointer
    }

    printf("Enter elements for array c:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", p_c + i);  // Accessing array c through pointer
    }

    printf("Enter elements for array d:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", p_d + i);  // Accessing array d through pointer
    }

    // Find the element-wise sum of a, b, c, and d into sumarray using pointers
    for (int i = 0; i < n; i++) {
        *(p_sum + i) = *(p_a + i) + *(p_b + i) + *(p_c + i) + *(p_d + i);
    }

    // Display the sumarray
    printf("The element-wise sum of the arrays is:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", *(p_sum + i));
    }
    printf("\n");

    return 0;
}
