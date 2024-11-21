#include <stdio.h>

int main() {
    // Declare and initialize the integer array
    int a[] = {10, 20, 30, 40, 50};
    int n = sizeof(a) / sizeof(a[0]); // Calculate the number of elements in the array

    // Display the address and value of each element
    printf("Index\tValue\t\tAddress\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t%d\t\t%p\n", i, a[i], (void*)&a[i]);
    }

    // Observations about address changes
    printf("\nObservation:\n");
    printf("The difference in addresses between consecutive elements is equal to the size of an integer (4 bytes on most systems).\n");

    return 0;
}
