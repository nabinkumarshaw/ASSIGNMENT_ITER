#include <stdio.h>

// Define the structure
struct Point {
    float x;
    float y;
    float z;
};

int main() {
    // Declare and initialize a structure variable
    struct Point point = {6.7, 1.2, 2.3};

    // Declare a pointer to the structure and initialize it
    struct Point *p = &point;

    // Display the values using the pointer
    printf("Values of x, y, and z using pointer p:\n");
    printf("x = %.1f\n", p->x);
    printf("y = %.1f\n", p->y);
    printf("z = %.1f\n", p->z);

    return 0;
}
