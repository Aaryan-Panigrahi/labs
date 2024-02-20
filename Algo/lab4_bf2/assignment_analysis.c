#include <stdio.h>
#include <stdlib.h>

void print2darr(int arr[4][4], int n){
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++)
            printf("%d  ", arr[i][j]);
        printf("\n");
    }
    printf("\n");
}

int fact(int n){
    if(n==0) return 1;
    return n * fact(n-1);
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void genpermutes(int* base, int start, int end, int** result, int *count){
    if(start == end){
        for(int i=0; i<end; i++){
            result[*count][i] = base[i];
        }
        (*count)++;
    }
    else{
        for(int i=start; i<end; i++){
            swap(&base[start], &base[i]);
            genpermutes(base, start+1, end, result, count);
            swap(&base[start], &base[i]);
        }
    }
}

int** permute(int n){

    int tot = fact(n);

    int base[n];
    for(int i=0; i<n; i++){
        base[i] = i+1;
    }

    int **mother = (int**) malloc(tot*sizeof(int *));
    for(int i=0; i<tot; i++){
        mother[i] = (int*) malloc(n*sizeof(int));
    }

    int count = 0;
    genpermutes(base, 0, n, mother, &count);

    if(count == tot){
        printf("\nAll permutations generated!!\n\n");
    }

    return mother;
}


void print2d(int **permutations, int n) {
    int totalPermutations = fact(n);
    for (int i = 0; i < totalPermutations; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", permutations[i][j]);
        }
        printf("\n");
    }
}

void test(){
    printf("Sample Case - \n");
    int sample_cost[4][4] = {9, 2, 7, 8, 6, 4, 3, 7, 5, 8, 1, 8, 7, 6, 9, 4};
    int n = 4;
    print2darr(sample_cost, n);

    int tot = fact(n);
    int **moth = permute(n);
    print2d(moth, n);

    int min = 9999999;
    int min_case[n];
    for(int i=0; i<tot; i++){
        int cost = 0;

        printf("Trying - ");
        for(int k=0; k<n; k++) printf("%d ", moth[i][k]);

        printf("\n");
        for(int j=0; j<n; j++){
            cost += sample_cost[j][moth[i][j] - 1];
        }
        if(cost < min){
            min = cost;
            for(int j=0; j<n; j++){
                min_case[j] = moth[i][j];
            }
        }
    }
    printf("Best Assignment with cost = %d is - \n", min);
    for(int i=0; i<n; i++){
        printf("Person %d gets Job %d \n", i+1, min_case[i]);
    }
}

int test2(int ** costs, int n){

    int opc = 0;
    int tot = fact(n);
    int **moth = permute(n);
    // print2d(moth, n);

    int min = 9999999;
    int min_case[n];
    for(int i=0; i<tot; i++){
        int cost = 0;

        printf("Trying - ");
        for(int k=0; k<n; k++) printf("%d ", moth[i][k]);

        printf("\n");
        for(int j=0; j<n; j++){
            opc++;
            cost += costs[j][moth[i][j] - 1];
        }
        if(cost < min){
            min = cost;
            for(int j=0; j<n; j++){
                min_case[j] = moth[i][j];
            }
        }
    }
    // printf("Best Assignment with cost = %d is - \n", min);
    // for(int i=0; i<n; i++){
    //     printf("Person %d gets Job %d \n", i+1, min_case[i]);
    // }
    return opc;
}

void analyze(){
    int * input_size = (int *) malloc(10 * sizeof(int));
    for(int i=0; i<10; i++){
        input_size[i] = (i+1);
    }
    int * op_counts = (int *) malloc(10 * sizeof(int));

    for(int i=0; i<10; i++){
        //generate random cost matrix of size 10*i
        int n = input_size[i];
        int ** costs = (int **) malloc(n * sizeof(int *));
        for(int j=0; j<n; j++){
            costs[j] = (int *) malloc(n * sizeof(int));
        }
        for(int j=0; j<n; j++){
            for(int k=0; k<n; k++){
                costs[j][k] = rand() % 100;
            }
        }
        op_counts[i] = test2(costs, n);
        printf("Operation Count for input size %d is %d\n", n, op_counts[i]);
    }
    printf("\n\nInput Size, Operation Count - \n");
    for(int i=0; i<10; i++){
        printf("%d, %d\n", input_size[i], op_counts[i]);
    }
}

int main(){
    analyze();
    
    test();
    int n, i, j;

    printf("\n\nEnter the number of persons and jobs (equal) ");
    scanf("%d", &n);

    int cost_mat[n][n];
    printf("\nEnter the cost matrix (persons -- rows)- \n");
    for(i=0; i<n; i++){
        for(j=0; j<n; j++)
            scanf("%d", &cost_mat[i][j]);
    }

    int tot = fact(n);
    int **moth = permute(n);

    int min = 9999999;
    int min_case[n];
    for(int i=0; i<tot; i++){
        int cost = 0;
        for(int j=0; j<n; j++){
            cost += cost_mat[j][moth[i][j]-1];
        }
        if(cost < min){
            min = cost;
            for(int j=0; j<n; j++){
                min_case[j] = moth[i][j];
            }
        }
    }
    printf("Best Assignment with cost = %d is- \n", min);
    for(int i=0; i<n; i++){
        printf("Person %d gets Job %d \n", i+1, min_case[i]);
    }

    


}