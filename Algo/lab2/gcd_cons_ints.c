#include<stdio.h>

int gcd1(int m, int n){
    int t = m, opcount = 0;
    //Assign min to t
    if(n<m) t = n;

    while(t>0){
        opcount++;
        if(n%t == 0 && m%t == 0){
            printf("Opcount = %d\n\n", opcount);
            return t;
        }
        t--;        
    }

}

int main(){
    int m, n;

    printf("Enter Both the numbers - \n");
    scanf("%d%d", &m, &n);

    printf("Sum m+n = %d\n", m+n);
    printf("GCD = %d\n", gcd1(m,n));

}