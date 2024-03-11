#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int *arr, int n){
    for(int i=0; i<n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

}

void tejas(int arr[], int n){
    for(int i=0; i<n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

}

int main(){
    int n;
    printf("Enter size");
    scanf("%d", &n);
    int *arr = malloc(n*sizeof(int));

    const int nc = n;
    int arr2[nc];

    for(int i=0; i<n; i++){
        scanf("%d", &arr[i]);
        scanf("%d", &arr2[i]);
    }

    tejas(arr2, n);

}