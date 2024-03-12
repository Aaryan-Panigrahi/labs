#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TABLE_SIZE 100 // Size of the hash table

typedef struct {
    bool isOccupied;
    int key;
} HashTableEntry;

// Hash function
int hash(int key) {
    return key % TABLE_SIZE;
}

// Insert a key into the hash table
void insert(HashTableEntry table[], int key) {
    int index = hash(key);
    int originalIndex = index;
    bool placed = false;

    while (table[index].isOccupied) {
        index = (index + 1) % TABLE_SIZE; // Linear probing
        if (index == originalIndex) { // Table is full
            return;
        }
    }

    table[index].isOccupied = true;
    table[index].key = key;
}

// Search for a key in the hash table
int search(HashTableEntry table[], int key, bool *found) {
    int index = hash(key);
    int originalIndex = index;
    int comparisons = 0;

    while (table[index].isOccupied) {
        comparisons++;
        if (table[index].key == key) {
            *found = true;
            return comparisons; // Key found
        }
        index = (index + 1) % TABLE_SIZE; // Linear probing
        if (index == originalIndex) { // Went through the whole table
            break;
        }
    }

    *found = false;
    return comparisons; // Key not found
}

int main() {
    HashTableEntry hashTable[TABLE_SIZE] = {0};
    bool found;
    int comparisons;

    // Example usage
    // Insert some keys into the hash table
    for (int i = 0; i < 50; ++i) {
        insert(hashTable, i * 2); // Insert even numbers
    }

    // Search for a key and count comparisons
    comparisons = search(hashTable, 10, &found); // Successful search
    printf("Successful search comparisons: %d\n", comparisons);

    comparisons = search(hashTable, 11, &found); // Unsuccessful search
    printf("Unsuccessful search comparisons: %d\n", comparisons);

    return 0;
}
