//Assignment 3
//1.WAP to create a linked list.
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
        printf("linked list (");
        while(tmp != NULL){
                printf("%d, ", tmp->data);
                tmp = tmp->next;
        }
        printf(")\n");
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

void menu(){
    printf("\nChoose one of the following:\n");
    printf("1.append\n2.display\n3.exit\n\n");
}


int main(){
    int val=1, num, choice;
    struct node *head = NULL;
    
    printf("\nLinked list creation:\n\n");
    while (val){
        menu();
       printf("\nwhat you choose (whole number between 1 to 3 (included)): ");
        scanf(" %d", &choice);
        switch (choice){
            case 1:
                printf("\nenter what to append : ");
                scanf("%d", &num);
                append(&head, num);
                break;
                
            case 2:
                print(head);
                break;
                
            case 3:
                val=0;
                break;
                
            default:
                printf("\nwrong choice\n");
                break;
        }
    }
    return 0;
}
