#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}node;

typedef struct graph{
    int n;
    node **adj_list;
}graph;

node *create_node(int data){
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

graph *create_graph(int n){
    graph *new_graph = (graph *)malloc(sizeof(graph));
    new_graph->n = n;
    new_graph->adj_list = (node **)malloc(n * sizeof(node *));
    for(int i = 0; i < n; i++){
        new_graph->adj_list[i] = NULL;
    }
    return new_graph;
}
//added this function
graph * create_graph_usr(){
    int n;
    printf("Enter the number of vertices: ");
    scanf("%d", &n);
    graph *new_graph = create_graph(n);
    printf("Enter the number of edges: ");
    int e;
    scanf("%d", &e);
    for(int i = 0; i < e; i++){
        printf("Enter the source and destination of edge %d: ", i+1);
        int src, dest;
        scanf("%d %d", &src, &dest);
        add_edge(new_graph, src, dest);
    }
    return new_graph;
}

void add_edge(graph *graph, int src, int dest){
    node *new_node = create_node(dest);
    new_node->next = graph->adj_list[src];
    graph->adj_list[src] = new_node;

    new_node = create_node(src);
    new_node->next = graph->adj_list[dest];
    graph->adj_list[dest] = new_node;
}

void print_adj_list(graph *graph){
    printf("\nAdjacency list:\n");
    for(int i = 0; i < graph->n; i++){
        node *temp = graph->adj_list[i];
        printf("V %d : ", i);
        while(temp){
            printf("%d -> ", temp->data);
            temp = temp->next;
        }
        printf("NULL\n");
    }
    printf("\n");
}
