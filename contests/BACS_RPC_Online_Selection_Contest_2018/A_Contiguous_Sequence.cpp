#include<bits/stdc++.h>
using namespace std;

int main(){
    long long T,N,s1,s2,s,ans=0;
    cin>>T;
    for(int i=1; i<=T; i++){
        cin>>N;
        cin>>s1;
        ans=0;
        N--;
        while(N--){
            cin>>s2;
            if(s2-s1==1)ans=1;
            s1=s2;
        }
        if(ans==1)cout<<"Case "<<i<<": Yes\n";
        else cout<<"Case "<<i<<": No\n";
    }
    return 0;
}
