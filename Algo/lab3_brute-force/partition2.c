#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(){
    printf("Enter the number of elements in the array: ");
    int n;
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements of the array: ");
    int sum = 0;
    for(int i = 0; i < n; i++){
        printf("\nEnter element %d: ", i + 1);
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    int power_set_size = pow(2, n);

    for(int counter = 0; counter < power_set_size; counter++){
        int temp_sum = 0;
        for(int j = 0; j < n; j++){
            if(counter & (1 << j)){
                temp_sum += arr[j];
            }
        }
        if(temp_sum == sum / 2){
            printf("The array can be partitioned into two subsets with equal sum.\n");
            printf("The subsets are:\n");
            for(int i = 0; i < n; i++){
                if(counter & (1 << i)){
                    printf("%d ", arr[i]);
                }
            }
            printf("\n");
            for(int i = 0; i < n; i++){
                if(!(counter & (1 << i))){
                    printf("%d ", arr[i]);
                }
            }
            return 0;
        }
    }
    printf("\nThe array cannot be partitioned into two subsets with equal sum.\n\n");

    

}