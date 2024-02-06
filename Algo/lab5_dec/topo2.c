#include <stdio.h>
#include <stdlib.h>
#include "graph.h"

void topo_source_rem(graph * g){

    printf("Starting indegs calc - ");
    // Calculate in degrees
    int indegs[g->n];
    for(int i = 0; i < g->n; i++){
        indegs[i] = 0;
    }
    for(int i = 0; i < g->n; i++){
        node * temp = g->adj_list[i];
        while(temp){
            indegs[temp->data] += 1;
            temp = temp->next;
        }
    }

    printf("\nInitial Indegs - ");
    for(int i=0; i<g->n; i++){
        printf("%d ", indegs[i]);
    }

    int topo_order[g->n];
    int index = 0;
    int visited[g->n];
    for(int i = 0; i < g->n; i++){
        visited[i] = 0;
    }

    // Find sources and add to topo
    for(int i = 0; i < g->n; i++){
        if(indegs[i] == 0){
            topo_order[index++] = i;
            visited[i] = 1;
        }
    }
    printf("\ntopo initial - ");
    for(int i=0; i<index; i++){
        printf("%d ", topo_order[i]);
    }

    while(index < g->n){

        if(index == g->n){
            printf("Graph has a cycle, so topoogical not possible!\n");
            return;
        }

        int u = topo_order[index-1];

        printf("u = %d\n", u);
        node * temp = g->adj_list[u];

        while(temp){
            indegs[temp->data] -= 1;
            if(indegs[temp->data] == 0 && !visited[temp->data]){
                topo_order[index++] = temp->data;
                visited[temp->data] = 1;
            }
            temp = temp->next;
        }
    }
    printf("\nTopological order: ");
    for(int i = 0; i < g->n; i++){
        printf("%d ", topo_order[i]);
    }
    printf("\n");
}

int main(){
    graph * g2 = create_graph_usr();

    // graph *g2 = create_graph(3);
    // add_edge(g2, 0, 1);
    // add_edge(g2, 0, 2);
    // add_edge(g2, 1, 2);

    print_adj_list(g2);
    
    topo_source_rem(g2);
}

