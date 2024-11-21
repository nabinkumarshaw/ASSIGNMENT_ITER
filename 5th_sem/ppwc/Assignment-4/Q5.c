#include <stdio.h>

// Define the structure
struct Numbers {
    int a;
    int b;
    int c;
};

int main() {
    // Declare and initialize a structure variable
    struct Numbers nums = {10, 20, 30};

    // Declare and initialize a pointer to the structure
    struct Numbers *ptr = &nums;

    // Update the values of a, b, and c through the pointer
    ptr->a += 10;
    ptr->b += 10;
    ptr->c += 10;

    // Display the updated values
    printf("Updated values of a, b, and c:\n");
    printf("a = %d\n", ptr->a);
    printf("b = %d\n", ptr->b);
    printf("c = %d\n", ptr->c);

    return 0;
}
