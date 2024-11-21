#include <stdio.h>
#include <ctype.h>  // For the toupper() function

#define MAX_STRINGS 5  // Define the maximum number of strings

int main() {
    // Declare an array of pointers to strings (array of character arrays)
    char *strings[MAX_STRINGS + 1] = {
        "hello", "world", "this", "is", "c", NULL
    };

    // Declare a pointer to the array of strings
    char **p = strings;

    // Iterate through each string in the array and convert to uppercase
    while (*p != NULL) {  // Loop until we encounter the NULL pointer
        char *str = *p;  // Get the current string
        char *ch = str;  // Pointer to traverse through each character in the string
        
        // Convert each character in the string to uppercase
        while (*ch != '\0') {  // Loop through each character of the string
            *ch = toupper(*ch);  // Convert to uppercase
            ch++;  // Move to the next character
        }
        
        p++;  // Move to the next string in the array
    }

    // Display the modified strings
    p = strings;  // Reset the pointer to the beginning of the array
    while (*p != NULL) {  // Loop until we encounter the NULL pointer
        printf("%s\n", *p);  // Print the current string
        p++;  // Move to the next string in the array
    }

    return 0;
}
