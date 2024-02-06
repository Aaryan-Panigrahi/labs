#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 1024

typedef struct{
    int size;
    int factor[MAX + 1];
    int expo[MAX + 1];
}prime_fact;

prime_fact factorise(int m){
    int i;
    int n=m, c=0;
    int k=1;

    prime_fact pf;
    pf.factor[0] = 1;
    pf.expo[0] = 1;

    for(i = 2; i <= n; i++){
        c=0;
        while(n%i == 0){
            c++;
            n /= i;
        }

        if(c>0){
            pf.expo[k] = c;
            pf.factor[k++] = i;
        }
    }

    pf.size = k;

    printf("\nPrime factors of %d - ", m);
    for(i=0; i<k; i++){
        printf("%d ^%d\t", pf.factor[i], pf.expo[i]);

    }


    return pf;
}

int gcd2(int m, int n){

    prime_fact mpf = factorise(m);
    prime_fact npf = factorise(n);
    int gcd = 1;
    int opcount = 0;

    int i=1, j=1;
    while(i < mpf.size && j < npf.size){
        opcount ++;
        if(mpf.factor[i] < npf.factor[j]) i++;
        else if(mpf.factor[i] > npf.factor[j]) j++;

        else{
            int minex = mpf.expo[i];
            if(mpf.expo[i] > npf.expo[j]) minex = npf.expo[j];

            for(int e=0; e<minex; e++) gcd *= mpf.factor[i];

            i++;
            j++;
        }
    }

    printf("\nOpcount = %d ", opcount);

    return gcd;
}

int main(){
    int m, n;

    printf("Enter Both the numbers - \n");
    scanf("%d%d", &m, &n);
    printf("Sum m+n = %d\n", m+n);
    printf("\nGCD = %d\n", gcd2(m,n));

}