// https://www.codechef.com/AUG18B/problems/SPELLBOB
#include<bits/stdc++.h>
using namespace std;
int sol(char t[], char b[]);
int main(){
    int T;
    char top[4],bot[4];
    scanf("%d",&T);
    while(T--){
        scanf("%s%s",top,bot);
        if(sol(top,bot))printf("yes\n");
        else printf("no\n");
    }
    return 0;
}
int sol(char t[], char b[]){
    int i=0,poso[3]={0,0,0};
    for(i=0; i<3; i++){
        if(!(t[i]=='b' || b[i]=='b' || t[i]=='o' || b[i]=='o'))return 0;
        if(t[i]=='o' || b[i]=='o')poso[i]=1;
    }
    if(poso[0]){
        if((t[1]=='b' || b[1]=='b')&&(t[2]=='b' || b[2]=='b'))return 1;
    }
    if(poso[1]){
        if((t[0]=='b' || b[0]=='b')&&(t[2]=='b' || b[2]=='b'))return 1;
    }
    if(poso[2]){
        if((t[1]=='b' || b[1]=='b')&&(t[0]=='b' || b[0]=='b'))return 1;
    }
    return 0;
}
