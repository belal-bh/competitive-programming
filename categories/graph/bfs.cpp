/* BFS represented in adjacency-list.
Basic code.
 */
#include<bits/stdc++.h>
using namespace std;

// adj[a].push_back(b); for an edge from a to b
vector<int> adj[100];
int vis[100]; // 0 if not visited, 1 if visited

/* s is the starting vertex and
 n is the number of vertices (0 ... n-1) */
void bfs(int s, int n){
    for(int i=0; i<n; i++)vis[i]=0;
    queue<int> Q;
    Q.push(s);
    vis[s]=1;
    printf("visit: %d\n",s);

    while(!Q.empty()){
        int u=Q.front();
        Q.pop();

        int adj_len= adj[u].size();
        for(int i=0; i<adj_len; i++){
            if(vis[adj[u][i]]==0){
                int v=adj[u][i];
                vis[v]=1;
                printf("visit: %d\n",v);
                Q.push(v);
            }
        }
    }
}

int main(){
    int n_v; // number of vertices
    //printf("Number of vertices(?):");
    scanf("%d",&n_v);
    /* considering the vertex are numbering as 0 , 1 , 2, ...., n-1
     and adj[a].push_back(b); for an edge from a to b */
    for(int a=0; a<n_v; a++){
        int b;
        int n_adj_v;
        /*printf("Enter number of adjacent-vartices of vertex-%d and those vertices respectivly:",a);*/
        scanf("%d",&n_adj_v);
        while(n_adj_v--){
            scanf("%d",&b);
            adj[a].push_back(b);
        }
    }
    int s=0; // source vertex s
    bfs(s,n_v);
    return 0;
}
