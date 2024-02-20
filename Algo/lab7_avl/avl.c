#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "tree.h"

// AVL Trees are like bsts (lower left, higher right)
// But you also have to maintain the balance of the tree by doing rotations

//The 4 rotations operations 

Tnode* left(Tnode* z){
    //This case is called when the new is on the right of right of r
    Tnode* y = z->rch;
    Tnode* x = y->rch;

    Tnode* temp = y->lch;
    y->lch = z;
    z->rch = temp;

    return y;
}

Tnode* right(Tnode* z){
    // when new is at left of left of z
    Tnode* y = z->lch;
    Tnode* x = y->lch;

    Tnode* temp = y->rch;
    y->rch = z;
    z->lch = temp;

    return y; //new root
}

Tnode* left_right(Tnode* z){
    //new is at left-right of z
    Tnode* y = z->lch;
    z->lch = left(y);
    return right(z);
}

Tnode* right_left(Tnode* z){
    //new at right-left
    Tnode* y = z->rch;
    z->rch = right(y);
    return left(z);
}

Tnode* insert_bst(Tnode* root, int key){
    Tnode* new = get_node(key);
    if(root == NULL)
        return new;
    
    if(key < root->key){
        root->lch = insert_bst(root->lch, key);
    }
    else if(key > root->key){
        root->rch = insert_bst(root->rch, key);
    }
    else
        printf("Duplicate keys not allowed!");
    
    return root;
}

int num_levels(Tnode* root){
    if (root == NULL) return 0;
    return 1 + max(num_levels(root->lch), num_levels(root->rch));
}

void calc_bfs(Tnode* root){
    if(root == NULL) return;
    root->bf = num_levels(root->lch) - num_levels(root->rch);
    calc_bfs(root->lch);
    calc_bfs(root->rch);
}

Tnode* insert_avl(Tnode* root, int key){
    root = insert_bst(root, key);
    calc_bfs(root);

    // 1. Re-navigate towards our key (bst search)
    // 2. On the way, check for bf ==2
    // 3. As soon as you find a bf ==2 remember it as a z
    //      The next two on your way are going to be y an x.
    //      Also keep track of your movement from z to x = {LL, RR, L}

}

