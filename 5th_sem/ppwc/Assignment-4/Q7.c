#include <stdio.h>

int main() {
    // Declare and initialize two variables
    int a = 15, b = 25;

    // Declare pointers pointing to the variables
    int *p1 = &a;
    int *p2 = &b;

    // Compare the values pointed to by the pointers and find the greater value
    if (*p1 > *p2) {
        printf("The greater value is: %d\n", *p1);
    } else {
        printf("The greater value is: %d\n", *p2);
    }

    return 0;
}

