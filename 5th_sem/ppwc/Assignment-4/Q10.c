#include <stdio.h>

// Define the structure
struct Data {
    int arr[5];
};

int main() {
    // Declare and initialize the structure variable
    struct Data data = {{10, 20, 30, 40, 50}}; // Array initialization inside the structure

    // Declare a pointer to the structure
    struct Data *ptr = &data;

    // Display the array content using the pointer
    printf("Array content using the pointer:\n");
    for (int i = 0; i < 5; i++) {
        printf("Element %d: %d\n", i, ptr->arr[i]);
    }

    return 0;
}
