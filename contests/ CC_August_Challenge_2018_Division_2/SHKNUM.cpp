// https://www.codechef.com/AUG18B/problems/SHKNUM
#include<bits/stdc++.h>
using namespace std;

typedef int ll;

/*pow and log2 func: https://stackoverflow.com/questions/3064926/how-to-write-log-base2-in-c-c */
ll lg2(ll x){
    int l=0;
    while (x >>= 1) { ++l; }
    return l;
}
ll p2(ll x){
    return 1<<x;
}
ll sol(ll n);
int main(){
    //printf("%d\n",INT_MAX ); //2147483647
    ll T,N;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&N);
        printf("%d\n",sol(N));
    }
    return 0;
}
ll sol(ll n){
    ll a,b,c,d,m,aa,bb,cc,dd,mm;
    if(n==1)return 2;
    a=lg2(n); aa=a+1;
    c=p2(a); cc=c+c;
    b=n-c; bb=cc-n;
    if(b==0)return 1;
    d=lg2(b); dd=0;
    m=abs(b-p2(d));
    mm=abs(bb+1);
    m=min(m,mm);
    return m;
}
