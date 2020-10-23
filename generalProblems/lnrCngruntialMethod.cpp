#include<iostream>
#define MAX_X 100

using namespace std;


int main(){
    long m,a,X[MAX_X];
    int X0=0;
    int j=0;
    int c=0;
    a=7;
    m=15;
    for(int i=1;i<5;i++){
        X[j]=X0=i;
        while(((a*X[j]+c)%m)!=X0){
            X[j+1]= (a*X[j]+c)%m;
            j++;
        }
        printf("\nFor X0= %d period is %d",X0,j+1);
        j=0;
    }
    return EXIT_SUCCESS;
}