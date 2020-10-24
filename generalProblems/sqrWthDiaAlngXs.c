#include<stdio.h>
#include<math.h>

int main(){
    printf("Hell's this World!\n");
    int i,j,n;
    printf("Enter no of lines for the square: ");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i>n/2){
                if(j==n-i/2||j==i/2)
                    printf("*");
                else
                {
                    printf(" ");
                }
            }
            else
            {   
                if(j==(n/2)-i||j==(n/2)+i)
                    printf("*");
                else
                {
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
    return 0;
}