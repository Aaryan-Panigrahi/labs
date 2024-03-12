#include <stdio.h>
#include <stdlib.h>

int keyComparisons = 0; // Global variable to track the number of key comparisons

typedef struct node {
    int key;
    struct node* next;
} Node;

// Hash function
int hash(int key, int m) {
    return key % m;
}

// Insert a key into the hash table
void insert(Node* hashTable[], int m, int key) {
    int index = hash(key, m);
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->next = NULL;

    if (hashTable[index] == NULL) {
        hashTable[index] = newNode;
    } else {
        Node* temp = hashTable[index];
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// Search for a key in the hash table
int search(Node* hashTable[], int m, int key) {
    int index = hash(key, m);
    Node* temp = hashTable[index];
    while (temp != NULL) {
        keyComparisons++; // Increment the key comparison count
        if (temp->key == key) {
            return 1; // Key found
        }
        temp = temp->next;
    }
    return 0; // Key not found
}

// Main function to test the hash table implementation
int main() {
    int mValues[] = {10, 20, 50}; // Hash table sizes
    int nValues[] = {50, 100, 200}; // Number of keys to insert

    for (int i = 0; i < 3; i++) { // Iterate over different hash table sizes
        int m = mValues[i];
        printf("Hash Table Size (m) = %d\n", m);
        
        for (int j = 0; j < 3; j++) { // Iterate over different numbers of keys
            int n = nValues[j];
            Node* hashTable[m];
            for (int k = 0; k < m; k++) {
                hashTable[k] = NULL;
            }

            // Insert n random keys into the hash table
            for (int k = 0; k < n; k++) {
                insert(hashTable, m, rand() % (n * 10)); // Assuming keys are within n*10
            }

            // Reset key comparisons count
            keyComparisons = 0;

            // Perform successful searches
            for (int k = 0; k < n; k++) {
                search(hashTable, m, rand() % (n * 10)); // Assuming keys are within n*10
            }
            printf("Successful Search \t Load Factor: %.2f \t Key Comparisons: %d\n", (float)n/m, keyComparisons);

            // Reset key comparisons count
            keyComparisons = 0;

            // Perform unsuccessful searches
            for (int k = 0; k < n; k++) {
                search(hashTable, m, (rand() % (n * 10)) + (n * 10)); // Keys outside the inserted range
            }
            printf("Unsuccessful Search \t Load Factor: %.2f \t Key Comparisons: %d\n", (float)n/m, keyComparisons);

            // Free memory
            for (int k = 0; k < m; k++) {
                Node* temp = hashTable[k];
                while (temp != NULL) {
                    Node* toDelete = temp;
                    temp = temp->next;
                    free(toDelete);
                }
            }
        }
    }
    return 0;
}
