#include <stdio.h>

// Define the structure
struct Data {
    int arr[5];
};

int main() {
    // Declare and initialize the structure variable with array values
    struct Data data = {{10, 20, 30, 40, 50}}; 

    // Declare a pointer to the structure and initialize it to point to 'data'
    struct Data *ptr = &data;

    // Display the array content using the pointer ptr
    printf("Array content using the pointer ptr:\n");
    for (int i = 0; i < 5; i++) {
        printf("Element %d: %d\n", i, ptr->arr[i]);
    }

    return 0;
}
