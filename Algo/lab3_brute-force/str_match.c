#include <stdio.h>
#include <string.h>

// Function to perform brute-force string matching
int bruteForceStringMatch(char* text, char* pattern) {
    int n = strlen(text);
    int m = strlen(pattern);

    for (int i = 0; i <= n - m; i++) {
        int j;
        for (j = 0; j < m; j++) {
            if (text[i + j] != pattern[j])
                break;
        }

        if (j == m)
            return i; // Pattern found at index i
    }

    return -1; // Pattern not found
}

int main() {
    char text[1000], pattern[100];
    
    printf("Enter the text: ");
    fgets(text, sizeof(text), stdin);
    printf("Enter the pattern: ");
    fgets(pattern, sizeof(pattern), stdin);

    // Removing newline characters from inputs
    text[strcspn(text, "\n")] = '\0';
    pattern[strcspn(pattern, "\n")] = '\0';

    int index = bruteForceStringMatch(text, pattern);

    if (index != -1)
        printf("Pattern found at index %d\n", index);
    else
        printf("Pattern not found in the text\n");

    return 0;
}
