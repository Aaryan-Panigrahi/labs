#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int *arr, int n){
    for(int i=1; i<n; i++){
        
        int val = arr[i];

        // You need to make shifts so that you have room to insert

        int j = i-1; //first in the sorted space behind us
        while(j>=0 && arr[j]>val){
            arr[j+1] = arr[j];
            j--;
        }
        // Either j = -1, or arr[j] < val - 
        // 1, 2, 3, 5, 8, j->10, <-[9], 11, 11
        // 1, 2, 3, 5, j->8,<-[9], 10, 10, 11
        
        // either way, the value j+1 can be overwritten
        arr[j+1] = val;
    }

}

int findFirst1(int *arr, int l, int h){
    int m = l + (h-l)/2;
    if(h>l){
        if((arr[m] == 1 && arr[m-1] == 0) || m == 0) return m;

        else if(arr[m] == 1) findFirst1(arr, l, m-1);
        else findFirst1(arr, m+1, h);
    }

}


int main(){
    int n;
    printf("Enter size - ");
    scanf("%d", &n);
    int *arr = malloc(n*sizeof(int));

    for(int i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    insertion_sort(arr, n);
    printf("Sorted - ");
    for(int i=0; i<n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

    int n0 = findFirst1(arr, 0, n-1);
    printf("Number of zeroes = %d", n0 );

}