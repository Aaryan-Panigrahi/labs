#include <stdio.h>
#include <stdlib.h>
#include "graph.h"

void topo_dfs_search(graph * g, int u, int * visited, int * topo, int * idx){
    visited[u] = 1;
    node * temp = g->adj_list[u];
    while(temp){
        if(!visited[temp->data]){
            topo_dfs_search(g, temp->data, visited, topo, idx);
        }
        temp = temp->next;
    }
    topo[*idx] = u;
    *idx -= 1;
}

void topo_dfs(graph * g){
    int visited[g->n];
    int topo[g->n];
    int idx = g->n - 1;
    for(int i = 0; i < g->n; i++){
        visited[i] = 0;
    }
    for(int i = 0; i < g->n; i++){
        if(!visited[i]){
            topo_dfs_search(g, i, visited, topo, &idx);
        }
    }
    printf("Topological order: ");
    for(int i = 0; i < g->n; i++){
        printf("%d ", topo[i]);
    }
    printf("\n");
}

int main(){
    // UNCOMMENT THIS TO TAKE USER-INPUT
    graph * g = create_graph_usr();

    //SAMPLE TESTCASE
    // graph *g = create_graph(5);
    // add_edge(g, 0, 1);
    // add_edge(g, 0, 4);
    // add_edge(g, 1, 2);
    // add_edge(g, 1, 3);
    // add_edge(g, 1, 4);
    // add_edge(g, 2, 3);
    // add_edge(g, 3, 4);

    topo_dfs(g);
}

