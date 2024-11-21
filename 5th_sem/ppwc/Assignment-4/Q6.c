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

    // Declare and initialize pointers for individual members
    int *pA = &nums.a;
    int *pB = &nums.b;
    int *pC = &nums.c;

    // Update the values of a, b, and c through their respective pointers
    *pA += 10;
    *pB += 10;
    *pC += 10;

    // Display the updated values
    printf("Updated values of a, b, and c:\n");
    printf("a = %d\n", *pA);
    printf("b = %d\n", *pB);
    printf("c = %d\n", *pC);

    return 0;
}
