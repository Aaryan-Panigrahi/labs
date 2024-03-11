#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int k;
    struct node* next;
}node;

typedef struct{
    int n;
    node ** adj_list;
}graph;

node* get_node(int key){
    node* new = (node*) malloc(sizeof(node));
    new->k = key;
    new->next = NULL;
    return new;
}

graph* create_graph(int nv){
    graph* g = (graph*) malloc(sizeof(graph));
    g->n = nv;
    g->adj_list = (node**) malloc(nv*sizeof(node*));
    for(int i=0; i<nv; i++){
        g->adj_list[i] = NULL;
    }
}

void add_edge(graph* g, int s, int d){
    node * new = get_node(d);
    new->next = g->adj_list[s];
    g->adj_list[s] = new;
}

void topo(graph* g){
    //calculate indegs
    int indegs = (int*) malloc(g->n * sizeof(int));

    //find indeg = 0
        // add to topo-list
        // 

}

int main(){
    graph *g = create_graph(4);
    add_edge(g, 0, 1);
    add_edge(g, 1, 2);
    add_edge(g, 2, 3);
    add_edge(g, 3, 0);

}