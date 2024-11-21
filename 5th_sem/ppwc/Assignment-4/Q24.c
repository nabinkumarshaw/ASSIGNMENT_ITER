#include <stdio.h>
#include <string.h>

void reverse_string(char *str) {
    // Pointers to the beginning and end of the string
    char *start = str;
    char *end = str + strlen(str) - 1;
    
    // Swap characters while the pointers haven't crossed
    while (start < end) {
        // Swap the characters
        char temp = *start;
        *start = *end;
        *end = temp;
        
        // Move the pointers towards the center
        start++;
        end--;
    }
}

int main() {
    char str[100];
    
    // Input string
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Remove newline character if present
    str[strcspn(str, "\n")] = '\0';
    
    // Reverse the string
    reverse_string(str);
    
    // Output the reversed string
    printf("Reversed string: %s\n", str);
    
    return 0;
}
