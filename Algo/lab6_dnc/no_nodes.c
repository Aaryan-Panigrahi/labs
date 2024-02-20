#include "tree.h"

int opcount = 0;

int count_nodes(Tnode* root) {
    opcount++;
    if (root == NULL) return 0;
    else {
        int left_count = count_nodes(root->lch);
        int right_count = count_nodes(root->rch);
        return left_count + right_count + 1;
    }
}

Tnode* generate_random_tree(int n) {
    if (n <= 0) return NULL;
    
    Tnode* root = get_node(rand() % 100); 

    root->lch = generate_random_tree(n / 2);
    root->rch = generate_random_tree(n - n / 2 - 1);

    return root;
}

// Function to analyze random trees of sizes 10, 20, ..., 100 nodes
void analyze() {
    static int op_counts[10]; 
    int tree_sizes[10];
    for(int i=0; i<10; i++) tree_sizes[i] = i*50;
    
    for (int i = 0; i < 10; i++) {
        Tnode* root = generate_random_tree(tree_sizes[i]);
        count_nodes(root); 
        op_counts[i] = opcount; 
        opcount = 0; 
    }
    
    printf("Size\tOpCount\n");
    for (int i = 0; i < 10; i++) {
        printf("%d\t%d\n", tree_sizes[i], op_counts[i]);
    }
}
int main() {
    analyze();

    // printf("\nUSER INPUT TREE \n");
    // printf("Enter the key for the root:");
    // int k;
    // scanf("%d", &k);
    Tnode* root = get_node(1);
    
    // // root = make_tree(root);

    //sample tree
    root->lch = get_node(2);
    root->rch = get_node(3);
    root->lch->lch = get_node(4);
    root->lch->rch = get_node(5);
    
    // Tnode* root = generate_random_tree(15);

    printf("Inorder: ");
    inorder(root); 
    printf("\nPreorder: ");
    preorder(root);
    printf("\nPostorder: ");
    postorder(root);
    printf("\n");
    printf("\n Number of nodes: %d\n", count_nodes(root));
    printf("Opcount = %d ", opcount);
    return 0;
}