#include <stdio.h>

// Define the structure
struct Point {
    int x;
    int y;
    int z;
};

int main() {
    // Declare and initialize a structure variable
    struct Point point = {10, 20, 30}; // Initial values for x, y, z

    // Declare and initialize pointers
    struct Point *p1 = &point; // p1 points to the structure
    struct Point *p2 = &point; // p2 points to the structure
    struct Point *p3 = &point; // p3 points to the structure

    // Display the value of x using pointer p1
    printf("Value of x from p1: %d\n", p1->x);

    // Update the value of x to 100 using pointer p3
    p3->x = 100;

    // Display the updated value of x
    printf("Updated value of x using p3: %d\n", p1->x);

    return 0;
}

