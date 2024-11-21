#include <stdio.h>

int find_largest(int *arr, int size) {
    int largest = *arr;  // Initialize largest with the first element
    for (int i = 1; i < size; i++) {
        if (*(arr + i) > largest) {
            largest = *(arr + i);  // Update largest if the current element is greater
        }
    }
    return largest;
}

int main() {
    int arr[100], size;
    
    // Input the size of the array
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    // Input the array elements
    printf("Enter the elements of the array: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    
    // Find the largest value using pointer
    int largest = find_largest(arr, size);
    
    // Output the largest value
    printf("The largest value in the array is: %d\n", largest);
    
    return 0;
}
