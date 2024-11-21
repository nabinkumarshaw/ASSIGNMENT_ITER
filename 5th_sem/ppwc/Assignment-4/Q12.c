#include <stdio.h>

// Define the structure
struct Data {
    int arr[5];
};

int main() {
    // Declare and initialize the structure variable with array values
    struct Data data = {{10, 20, 30, 40, 50}};

    // Declare a pointer to the array (pointer to int)
    int *ptr = data.arr;  // Here ptr is directly assigned to the array 'arr'

    // Display the array content using the pointer ptr
    printf("Array content using the pointer ptr:\n");
    for (int i = 0; i < 5; i++) {
        printf("Element %d: %d\n", i, *(ptr + i));  // Pointer arithmetic to access elements
    }

    return 0;
}
