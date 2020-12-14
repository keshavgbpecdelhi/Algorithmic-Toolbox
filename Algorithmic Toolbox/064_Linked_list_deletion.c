//Assignment 3
//2.WAP to perform deletion from the linked list.
//keshav 64
# include <stdio.h>
# include <stdlib.h>

struct node{
    int data;
    struct node *next;
};


void print(struct node *head){
    struct node *tmp;
    printf("\nlinked list status:\n\n");
    if(head == NULL){
        printf("empty list\n");
    }else{
        tmp = head;
        printf("linked list(");
        while(tmp != NULL){
                printf("%d, ", tmp->data);
                tmp = tmp->next;
        }
        printf(")");
    }
}


void append(struct node** ptr, int new_data) { 
    struct node* new_node = (struct node*) malloc(sizeof(struct node)); 
    struct node *last = *ptr;
    new_node->data  = new_data; 
    new_node->next = NULL; 
    if (*ptr == NULL) { 
       *ptr = new_node; 
       return; 
    }   
    while (last->next != NULL){ 
        last = last->next; 
    }
    last->next = new_node; 
    return;     
}


void delete(struct node **ptr, int to_delete) {
    if (*ptr == NULL){
        printf("underflow");
        return;
    }
    struct node *temp = *ptr;
    if (temp->data == to_delete){
        *ptr = temp->next;
        free(temp);
        return;
    }
    while (temp->next->data != to_delete){
        if (temp->next->next == NULL && temp->next->data!=to_delete){
            printf("\nnumber of elements are %d!!\n", to_delete);
            return;
        }
        temp = temp->next;
    }
    struct node *new_node = temp->next->next;
    free(temp->next);
    temp->next = new_node;    
}


void menu(){
    printf("\nChoose one of the following:\n");
    printf("1.append\n2.delete\n3.display\n4.exit\n\n");
}


int main(){
    int num, val=1, choice;
    struct node *head = NULL;
    
    printf("\nDeleting a node from linked list\n\n");
    while (val){
        menu();
         printf("\nwhat you choose (whole number between 1 to 3 (included)): ");
        scanf(" %d", &choice);
        switch (choice){
            case 1:
                printf("\nvalue to append: ");
                scanf("%d", &num);
                append(&head, num);
                break;
                
            case 2:
                printf("\nvalue to delete: ");
                scanf("%d", &num);
                delete(&head, num);
                break;
                
            case 3:
                print(head);
                break;
                
            case 4:
                val=0;
                break;
                
            default:
                printf("\nwrong choice\n");
                break;
        }
    }
    return 0;
}
