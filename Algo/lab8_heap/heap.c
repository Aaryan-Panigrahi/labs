#include<stdio.h>
#include<stdlib.h>


// In a binary tree, for a node i - 
//      Children are 2i & 2i+1
//      Parent = floor(i/2)
// So first n/2 elements are parents

void heapBottomUp(int *arr, int n){

    //for every parent node - 
    for(int i = n/2; i>0; i--){
        int j = 2*i;
        if(j < n) {// this is true if there are 2 children 
            if(arr[j + 1] > arr[j]) j = j+1;
        }
        // Now we need to check and possibly swap j with i (the parent)

        if(arr[i]<arr[j]){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

    }
}

int main(){

}