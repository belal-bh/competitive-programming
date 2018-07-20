#include<bits/stdc++.h>
using namespace std;

int main(){
    long T,N,Q,P;
    long long X,Y;
    scanf("%ld",&T);

    for(int i=1; i<=T; i++){
        scanf("%ld%ld",&N,&Q);
        long long a[N+3];
        for(int j=1; j<=N; j++){
            scanf("%lld",&a[j]);
        }
        for(int k=1; k<=Q; k++){
            scanf("%ld%lld%lld",&P,&X,&Y);
            if(P==1 && Y!=0){
                for(int l=1; l<=N; l++){
                    if(a[l]<=X){
                        a[l]-=Y;
                    }
                }
            }
            else if(P==2 && Y!=0){
                for(int l=1; l<=N; l++){
                    if(a[l]>=X){
                        a[l]+=Y;
                    }
                }
            }
        }
        for(int j=1; j<N; j++){
            printf("%lld ",a[j]);
        }
        printf("%lld\n",a[N]);
    }
    return 0;
}
