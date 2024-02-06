#include <stdio.h>
#include <stdlib.h>
#include "graph.h"

void topo_dfs_search(graph * g, int u, int * visited, int * topo_order, int * index){
    visited[u] = 1;
    node * temp = g->adj_list[u];
    while(temp){
        if(!visited[temp->data]){
            topo_dfs_search(g, temp->data, visited, topo_order, index);
        }
        temp = temp->next;
    }
    topo_order[*index] = u;
    *index -= 1;
}

void topo_dfs(graph * g){
    int visited[g->n];
    int topo_order[g->n];
    int index = g->n - 1;
    for(int i = 0; i < g->n; i++){
        visited[i] = 0;
    }
    for(int i = 0; i < g->n; i++){
        if(!visited[i]){
            topo_dfs_search(g, i, visited, topo_order, &index);
        }
    }
    printf("Topological order: ");
    for(int i = 0; i < g->n; i++){
        printf("%d ", topo_order[i]);
    }
    printf("\n");
}

void topo_source_rem(graph * g){
    // Calculate in degrees
    int indegree[g->n];
    for(int i = 0; i < g->n; i++){
        indegree[i] = 0;
    }
    for(int i = 0; i < g->n; i++){
        node * temp = g->adj_list[i];
        while(temp){
            indegree[temp->data] += 1;
            temp = temp->next;
        }
    }

    int count = 0;
    int topo_order[g->n];
    int index = 0;
    int visited[g->n];
    for(int i = 0; i < g->n; i++){
        visited[i] = 0;
    }

    // Find sources
    for(int i = 0; i < g->n; i++){
        if(indegree[i] == 0){
            topo_order[index++] = i;
            visited[i] = 1;
        }
    }
    while(count < g->n){

        if(index == g->n){
            printf("Graph has a cycle, so topoogical not possible!\n");
            return;
        }

        int u = topo_order[count];
        node * temp = g->adj_list[u];
        while(temp){
            indegree[temp->data] -= 1;
            if(indegree[temp->data] == 0 && !visited[temp->data]){
                topo_order[index++] = temp->data;
                visited[temp->data] = 1;
            }
            temp = temp->next;
        }
        count += 1;
    }
    printf("Topological order: ");
    for(int i = 0; i < g->n; i++){
        printf("%d ", topo_order[i]);
    }
    printf("\n");
}

int main(){
    // graph * g = create_graph_usr();

    graph *g = create_graph(5);
    add_edge(g, 0, 1);
    add_edge(g, 0, 4);
    add_edge(g, 1, 2);
    add_edge(g, 1, 3);
    add_edge(g, 1, 4);
    add_edge(g, 2, 3);
    add_edge(g, 3, 4);
    topo_dfs(g);
    
    topo_source_rem(g);
}

