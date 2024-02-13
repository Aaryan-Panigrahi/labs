#include <stdio.h>
#include <stdlib.h>

int opcount = 0;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int l, int h) {
    int piv = arr[h]; //pivoting wrt last element
    int idx_sm = l - 1; //idx of smaller - correct pos of pivot so far...

    for (int i = l; i < h; i++) {
        opcount++;
        if (arr[i] < piv) {
            idx_sm++;
            swap(&arr[idx_sm], &arr[i]);
        }
    }
    swap(&arr[idx_sm + 1], &arr[h]);
    return idx_sm + 1;
}

void quick_sort(int arr[], int l, int h){
    if(l<h){
        int piv = partition(arr, l, h);

        quick_sort(arr, l, piv-1);
        quick_sort(arr, piv+1, h);
    }
    return;
}
void printarr(int arr[], int n){
    for(int i=0; i<n; i++)
        printf(" %d", arr[i]);
    printf("\n");
}

void generate_random_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 1000; 
    }
}

void analyze() {
    static int op_counts[10]; 
    int array_sizes[10];
    for(int i=0; i<10; i++) array_sizes[i] = i*500;

    for (int i = 0; i < 10; i++) {
        int arr[array_sizes[i]];
        generate_random_array(arr, array_sizes[i]); 
        quick_sort(arr, 0, array_sizes[i] - 1); 

        op_counts[i] = opcount; 
        opcount = 0;

    }

    // Print operation counts in a table
    printf("Array Size\tOperation Count\n");
    for (int i = 0; i < 10; i++) {
        printf("%d\t\t%d\n", array_sizes[i], op_counts[i]);
    }
}

int main() {
    analyze();
    int n = 5;
    // int arr[] = {2, 1, 3, 7, 6};
    
    //usr input
    printf("Enter n - ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements - \n");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    
    //sort & print
    quick_sort(arr, 0, n-1);
    for (int i = 0; i < n; i++) 
        printf("%d ", arr[i]);
}
