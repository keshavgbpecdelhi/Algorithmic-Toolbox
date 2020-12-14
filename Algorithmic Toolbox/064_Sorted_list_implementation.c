//Assignment 3
//3.WAP to implement insertion. Deletion and Display operations on the sorted linked list. 
//keshav 64


# include <stdio.h>
# include <stdlib.h>

struct node{
    int data;
    struct node *next;
};


void print(struct node *head){
    struct node *tmp;
    printf("\nlink list goes like\n\n");
    if(head == NULL){
        printf("empty list\n");
    }else{
        tmp = head;
        printf("Linked List (");
        while(tmp != NULL){
                printf("%d, ", tmp->data);
                tmp = tmp->next;
        }
        printf(")\n");
    }
}


struct node *make_node(int num){
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = num;
    new_node->next = NULL;
    return new_node;
}


void sort_insert(struct node **ptr, struct node *to_insert){
    struct node *temp;
    if (*ptr==NULL || ((*ptr)->data)>=to_insert->data){
        to_insert->next = *ptr;
        *ptr = to_insert;
    } else {
        temp = *ptr;
        while (temp->next!=NULL && temp->next->data<=to_insert->data)
            temp = temp->next;    
        to_insert->next = temp->next;
        temp->next = to_insert;
    }
}


void sort_delete(struct node **ptr, int to_delete) {
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
    while (temp->next->data < to_delete){
        if (temp->next->next == NULL && temp->next->data<to_delete){
            printf("\nNo element with value %d found!!\n", to_delete);
            return;
        }
        temp = temp->next;
    }
    if (temp->next->data != to_delete){
        printf("\nnumber of elements are %d!!\n", to_delete);
        return;
    }
    struct node *new_node = temp->next->next;
    free(temp->next);
    temp->next = new_node;    
}


void menu(){
    printf("\nChoose one of the following:\n");
    printf("1.insertion\n2.deletion\n3.display\n4.exit\n\n");
}

int main(){
    int choice=0, val=1, num;
    struct node *head = NULL;
    printf("\ninseting, deleting and display in linked list.n\n");
    while (val){
        menu();
        printf("\nwhat you choose (whole number between 1 to 4 (included)): ");
        scanf(" %d", &choice);
        switch (choice){
        case 1:
            printf("\nEnter value for insertion in linked list: ");
            scanf("%d", &num);
            struct node *new_node = make_node(num);
            sort_insert(&head, new_node);
            break;
            
        case 2:
            printf("\nvalue to delete: ");
            scanf("%d", &num);
            sort_delete(&head, num);
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
}