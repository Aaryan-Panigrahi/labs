#include <stdio.h>
#include <string.h>

#define MAX 256 

int opc = 0;

void make_shiftTable(char pattern[], int shiftTable[]) {
    int m = strlen(pattern);
    for (int i = 0; i < MAX; i++) {
        shiftTable[i] = m; // initialize all with the length of the pattern
    }
    for (int i = 0; i < m - 1; i++) {
        shiftTable[(unsigned char)pattern[i]] = m - 1 - i; 
    }
}


int horspool(char text[], char pattern[]) {
    int shiftTable[MAX];
    int m = strlen(pattern);
    int n = strlen(text);
    opc = 0;

    make_shiftTable(pattern, shiftTable);

    int i = m - 1; // Position to align pattern's right end with text's right end

    while (i < n) {
        int k = 0;
        while (k < m && pattern[m - 1 - k] == text[i - k]) {
            k++;
            opc++;
        }
        if (k == m) return i - m + 1; // Pattern found at position (i - m + 1)
        else opc ++; // increment for last comparison
        
        // Shift the pattern
        i += shiftTable[(unsigned char)text[i]]; 
    }

    return -1; // Pattern not found
}

int main() {
    char text[] = "I did da Hoflee HOO";
    char pattern[] = "Hofle";

    int position = horspool(text, pattern);

    if (position != -1) {
        printf("Pattern found at position: %d\n", position);
    } else {
        printf("Pattern not found.\n");
    }

    printf("Number of key comparisons: %d\n", opc);

    return 0;
}
