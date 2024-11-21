#include <stdio.h>

// Define a structure to hold four integer variables
struct Values {
    int a;
    int b;
    int c;
    int d;
};

int main() {
    // Declare and initialize the structure
    struct Values values = {55, 105, 89, 68};

    // Declare pointers to the variables in the structure
    int *p_a = &values.a;
    int *p_b = &values.b;
    int *p_c = &values.c;
    int *p_d = &values.d;

    // Find the maximum among a, b, c, and d using pointers
    int *max = p_a; // Assume 'a' is the maximum initially

    if (*p_b > *max) {
        max = p_b;  // Update max if b is greater
    }
    if (*p_c > *max) {
        max = p_c;  // Update max if c is greater
    }
    if (*p_d > *max) {
        max = p_d;  // Update max if d is greater
    }

    // Store the maximum value in a variable
    int maximum = *max;

    // Display the maximum value
    printf("The maximum value is: %d\n", maximum);

    return 0;
}
