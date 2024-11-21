#include <stdio.h>

int main() {
    // Declare and initialize two arrays
    int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {10, 20, 30, 40, 50};
    int size1 = sizeof(arr1) / sizeof(arr1[0]); // Number of elements in arr1
    int size2 = sizeof(arr2) / sizeof(arr2[0]); // Number of elements in arr2

    // Print values and addresses of elements in arr1
    printf("Array 1:\n");
    printf("Index\tValue\t\tAddress\n");
    for (int i = 0; i < size1; i++) {
        printf("%d\t%d\t\t%p\n", i, *(arr1 + i), (void*)(arr1 + i));
    }

    // Print values and addresses of elements in arr2
    printf("\nArray 2:\n");
    printf("Index\tValue\t\tAddress\n");
    for (int i = 0; i < size2; i++) {
        printf("%d\t%d\t\t%p\n", i, *(arr2 + i), (void*)(arr2 + i));
    }

    return 0;
}
