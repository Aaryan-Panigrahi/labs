#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to perform Bubble Sort on an array
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

// Function to print an array
void printArray(int arr[], int size) {
    for (int i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // Allocate memory for the array
    int *arr = (int*)malloc(n * sizeof(int));

    // Generate random values for the array
    srand(time(NULL));
    for (int i = 0; i < n; i++)
        arr[i] = rand() % 1000;

    printf("Unsorted array: ");
    printArray(arr, n);

    // Measure time taken for sorting
    clock_t start_time = clock();
    bubbleSort(arr, n);
    clock_t end_time = clock();

    printf("Sorted array: ");
    printArray(arr, n);

    // Calculate time taken in seconds
    double time_taken = ((double)(end_time - start_time))/CLOCKS_PER_SEC;
    printf("Time taken: %f seconds\n", time_taken);

    // Plotting using gnuplot
    FILE *gnuplotPipe = popen("gnuplot -persistent", "w");
    fprintf(gnuplotPipe, "plot '-' with lines title 'Bubble Sort'\n");
    fprintf(gnuplotPipe, "%d %f\n", n, time_taken);
    fprintf(gnuplotPipe, "e\n");
    fclose(gnuplotPipe);

    // Free allocated memory
    free(arr);

    return 0;
}
