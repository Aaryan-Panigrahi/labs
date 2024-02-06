#include "graph.h"

void bfs(graph *g){
    int visited[g->n];
    int queue[g->n];
    int visit_order[g->n];
    int front = -1;
    int rear = -1;

    for(int i = 0; i < g->n; i++){
        visited[i] = 0;
    }

    queue[++rear] = 0;
    visited[0] = 1;
    while(front != rear){
        int u = queue[++front];
        visit_order[front] = u;
        node *temp = g->adj_list[u];
        while(temp){
            if(!visited[temp->data]){
                queue[++rear] = temp->data;
                visited[temp->data] = 1;
            }
            temp = temp->next;
        }
    }

    printf("Visit order: ");
    for(int i = 0; i < g->n; i++){
        printf("%d ", visit_order[i]);
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

    bfs(g);
}
