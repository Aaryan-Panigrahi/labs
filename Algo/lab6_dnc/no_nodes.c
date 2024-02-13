#include "tree.h"

int count_nodes(Tnode* root) {
    if (root == NULL) return 0;
    else {
        int left_count = count_nodes(root->lch);
        int right_count = count_nodes(root->rch);
        return left_count + right_count + 1;
    }
}

int main() {
    printf("Enter the key for the root:");
    int k;
    scanf("%d", &k);
    Tnode* root = get_node(k);
    
    // root = make_tree(root);

    //sample tree
    root->lch = get_node(2);
    root->rch = get_node(3);
    root->lch->lch = get_node(4);
    root->lch->rch = get_node(5);

    printf("Inorder: ");
    inorder(root);
    printf("\nPreorder: ");
    preorder(root);
    printf("\nPostorder: ");
    postorder(root);
    printf("\n");
    printf("\n Number of nodes: %d\n", count_nodes(root));
    return 0;
}