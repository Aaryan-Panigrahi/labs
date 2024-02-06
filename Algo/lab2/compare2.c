#include<stdio.h>
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

    // printf("\nPrime factors of %d - ", m);
    // for(i=0; i<k; i++){
    //     printf("%d ^%d\t", pf.factor[i], pf.expo[i]);

    // }


    return pf;
}

int gcd2(int m, int n){
    int opcount = 0;
    prime_fact mpf = factorise(m);
    prime_fact npf = factorise(n);
    int gcd = 1;
    

    int i=1, j=1;
    while(i < mpf.size && j < npf.size){
        
        if(mpf.factor[i] < npf.factor[j]) i++;
        else if(mpf.factor[i] > npf.factor[j]) j++;

        else{
            int minex = mpf.expo[i];
            if(mpf.expo[i] > npf.expo[j]) minex = npf.expo[j];

            for(int e=0; e<minex; e++){
                opcount ++;
                gcd *= mpf.factor[i];
            }
            i++;
            j++;
        }
    }

    printf("\nOpcount = %d ", opcount);

    return opcount;
}

int gcd1(int m, int n){
    int t = m, opct = 0;
    //Assign min to t
    if(n<m) t = n;

    while(t>0){
        opct++;
        if(n%t == 0 && m%t == 0){
            printf("GCD = %d\n\n", t);
            return opct;
        }
        t--;        
    }

}
int main(){
    int n,m;
	int m_plus_n[10], opcounts1[10], opcounts2[10];
 
	for(int i=0;i<10;i++){
		printf("\nEnter the two numbers whose GCD has to be calculated:\n");
		scanf("%d %d", &n, &m);
		opcounts1[i] = gcd1(n,m);
        opcounts2[i] = gcd2(n,m);
		m_plus_n[i] = m+n;
	}

    for(int i=0;i<10;i++){
		printf("%d, ", m_plus_n[i]);
	}
    printf("\n");

	for(int i=0;i<10;i++){
		printf("%d, ", opcounts1[i]);
	}
	printf("\n");

    for(int i=0;i<10;i++){
		printf("%d, ", opcounts2[i]);
	}
	printf("\n");
	
}