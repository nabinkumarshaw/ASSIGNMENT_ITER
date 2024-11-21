#include <stdio.h>

int main() {
    // Declaring two integer variables and assigning values
    int a = 10, b = 20;

    // Printing the initial values and addresses
    printf("Before Swap:\n");
    printf("Variable a: Value = %d, Address = %p\n", a, (void*)&a);
    printf("Variable b: Value = %d, Address = %p\n", b, (void*)&b);

    // Swapping the contents of the variables
    int temp = a;
    a = b;
    b = temp;

    // Printing the values and addresses after swapping
    printf("\nAfter Swap:\n");
    printf("Variable a: Value = %d, Address = %p\n", a, (void*)&a);
    printf("Variable b: Value = %d, Address = %p\n", b, (void*)&b);

    // Checking if the addresses before and after are the same
    printf("\nAddresses remain the same before and after swap:\n");
    printf("Address of a: %p\n", (void*)&a);
    printf("Address of b: %p\n", (void*)&b);

    return 0;
}
