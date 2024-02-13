#include <stdio.h>
#include <stdlib.h>

int opcount = 0;

void printarr(int arr[], int n){
    for(int i=0; i<n; i++)
        printf(" %d", arr[i]);
    printf("\n");
}

void merge(int arr[], int l, int m, int h){
    
    // 1. Splits arr into 2 and stores them in la and ha 
    //     (These two are assumed to be already sorted)
    //     la = arr[l...m-1]
    //     ha = arr[m...h-1]

    // 2. Merges la and ha into a sorted arr

    int nla = m-l+1;
    int nha = h-m;
    
    int la[nla], ha[nha];
    int li, hi, ai;

    //copy to new lists
    for(li = 0; li<nla; li++) la[li] = arr[l+li];
    for(hi = 0; hi<nha; hi++) ha[hi] = arr[m+1 + hi];
    
    //merge both and overwrite arr[ai]
    li = 0; hi = 0; ai = l;

    while(li < nla && hi < nha){
        opcount++;  
        if(la[li] < ha[hi]) arr[ai++] = la[li++];
        else arr[ai++] = ha[hi++]; 
    }
    // remaining elements
    while(li<nla) arr[ai++] = la[li++];
    while(hi<nha) arr[ai++] = ha[hi++];
    
}

void mergeSort(int arr[], int l, int h){
    if(l<h){
        int m = l + (h-l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, h);

        merge(arr, l, m, h);
    }
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
        mergeSort(arr, 0, array_sizes[i] - 1); 

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
    
    // usr input
    printf("Enter n - ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements - \n");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    
    //sort & print
    mergeSort(arr, 0, n-1);
    for (int i = 0; i < n; i++) 
        printf("%d ", arr[i]);
}
