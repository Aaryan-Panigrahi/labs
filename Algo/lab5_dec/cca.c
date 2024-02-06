#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	int key;
	struct node* lch;
	struct node* rch;
}Tnode;

Tnode* get_node(int k){
	Tnode* t = (Tnode*) malloc(sizeof(Tnode));
	t->key = k;
	t->lch = NULL;
	t->rch = NULL;
	return t;
}

void inorder(Tnode* rt){
	if(rt == NULL) return;
	inorder(rt->lch);
	printf("%d ", rt->key);
	inorder(rt->rch);
}

void preorder(Tnode* rt){
	if(rt == NULL) return;

	printf("%d ", rt->key);
	preorder(rt->lch);
	preorder(rt->rch);
}

void postorder(Tnode* rt){
	if(rt == NULL) return;

	postorder(rt->lch);
	postorder(rt->rch);
	printf("%d ", rt->key);
}

Tnode* make_tree(Tnode* root){
    
    //Input a root that already has a key
    
	
    int choice, k;
    Tnode *temp, *ptr;
    ptr = root;

    printf("Tree-create MENU - \n1. Insert Left\n2. Insert Right\n3. Move Up\n4. Exit\n");

    while(1) {
        Tnode* parent = ptr;
        printf("\nCurrently at - %d", ptr->key);
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                if (ptr->lch == NULL) {
                    printf("Enter the key for the left child: ");
                    scanf("%d", &k);
                    temp = get_node(k);
                    ptr->lch = temp;
                    ptr = temp;
                } else {
                    printf("Left child already exists. Moving to left child.\n");
                    ptr = ptr->lch;
                }
                break;
            case 2:
                if (ptr->rch == NULL) {
                    printf("Enter the key for the right child: ");
                    scanf("%d", &k);
                    temp = get_node(k);
                    ptr->rch = temp;
                    ptr = temp;
                } else {
                    printf("Right child already exists. Moving to right child.\n");
                    ptr = ptr->rch;
                }
                break;
            case 3:
                printf("Moving up to the root.\n");
                ptr = root;
                break;
            case 4:
                printf("Exiting tree creation.\n");
                return root;
            default:
                printf("Invalid choice.\n");
        }
    }
}

Tnode* find_cca(Tnode* root, int key1, int key2) {
    if (root == NULL) return NULL; //If one of the keys is not there also
    
    if (root->key == key1 || root->key == key2)
        return root;

    Tnode* left = find_cca(root->lch, key1, key2);
    Tnode* right = find_cca(root->rch, key1, key2);

    //You will find the keys on different sides - left & right @ cca
    if (left && right)
        return root;
    
    return (left != NULL) ? left : right;
}


int main(){
    printf("\nEnter value for root node - ");
    int rk;
    scanf("%d", &rk);

    Tnode * rt = get_node(rk);
    make_tree(rt);
    printf("Tree created!\n");
    printf("Inorder - ");
    inorder(rt);

    printf("Now let's Find Common Ancestors!!");
    printf("\nEnter keys -1, -1 to exit\n");

    while(1){
        printf("Enter 2 keys to find the closest ancestor of - ");
        int k1, k2;
        scanf("%d%d", &k1, &k2);
        if(k1==-1 && k2==-1) return 0;

        Tnode* cca = find_cca(rt, k1, k2);
        if(cca == NULL) printf("\nOne of the keys was not there :(\n");
        else{
            printf("CCA of %d & %d is - %d\n", k1, k2, cca->key);
        }

    }
    

}
