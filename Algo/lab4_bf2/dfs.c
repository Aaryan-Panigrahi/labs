#include "graph.h"

void dfs_visit(graph *g, int u, int *visited, int *push_order, int *pop_order, int *push_index, int *pop_index){
    visited[u] = 1;
    push_order[*push_index] = u;
    *push_index += 1;

    node *temp = g->adj_list[u];
    while(temp){
        if(!visited[temp->data]){
            dfs_visit(g, temp->data, visited, push_order, pop_order, push_index, pop_index);
        }
        temp = temp->next;
    }

    pop_order[*pop_index] = u;
    *pop_index += 1;
}

void dfs(graph *g){
    int visited[g->n];
    int push_order[g->n];
    int pop_order[g->n];
    int push_index = 0;
    int pop_index = 0;
    
    for(int i = 0; i < g->n; i++){
        visited[i] = 0;
    }

    for(int i = 0; i < g->n; i++){
        if(!visited[i]){
            dfs_visit(g, i, visited, push_order, pop_order, &push_index, &pop_index);
        }
    }
    printf("Push order: ");
    for(int i = 0; i < g->n; i++){
        printf("%d ", push_order[i]);
    }
    printf("\nPop order: ");
    for(int i = 0; i < g->n; i++){
        printf("%d ", pop_order[i]);
    }
}



int main(){

    //make a graph
    graph *g = create_graph(5);
    add_edge(g, 0, 1);
    add_edge(g, 0, 4);
    add_edge(g, 1, 2);
    add_edge(g, 1, 3);
    add_edge(g, 1, 4);
    add_edge(g, 2, 3);
    add_edge(g, 3, 4);

    print_adj_list(g);

    dfs(g);
}