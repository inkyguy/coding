#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void createlist();
void display();
void insert();
void insertend();
void insertbeginning();
void reverse();
void del();
void deletemid();

struct node{
    int data;
    struct node *next;  //self referential structure
};
struct node *head =NULL;

//1
void createlist(){
    int data1;
    char ch='y';
    struct node *temp,*ptr =head;

    while(ch=='y'){
        temp=(struct node *)malloc(sizeof(struct node));
        printf("enter the data: ");
        scanf("%d",&data1);
        temp->data=data1;
        temp->next=NULL;

        if(head==NULL){
            head=temp;
        }
        else{
            ptr=head;
            while(ptr->next!=NULL){
                ptr=ptr->next;
            }
            ptr->next=temp;//pointer increment
            
        }
    printf("do you want to continue? y/n \n");
    scanf("%s",&ch);
    }
    //free(ptr);
}

//2
void display(){
    struct node *temp=head;
    //temp=head;
  //  if(head==NULL){
  //      printf("list is empty");
  //  }
    //else{
    while (temp!=NULL){
        printf("%d-->",temp->data);
        temp=temp->next;
        //printf("-->");
    }
   // }
   printf(" NULL \n");
   //free(temp);
}

//3
void insert(){
    int ele;
    struct node *temp,*ptr=head;
    temp=(struct node*)malloc(sizeof(struct node));
    printf("enter the data: \n");
    scanf("%d",&temp->data);
    temp->next=NULL;
    printf("enter the element: \n");
    scanf("%d",&ele);

    while(ptr!=NULL){
        if(ptr->data ==ele){
            if(ptr->next!=NULL){
                temp->next=ptr->next;
                ptr->next=temp; 
                break;
            }
            else{
                ptr->next=temp; 
                temp->next=NULL; 
                break;
            }
        }
        else{
            ptr=ptr->next;
        }
    }
    //free(ptr);
}

//4
void del(){
    printf("function rasinaka call chey ra naina :/ \n");
}

void insertend(){
    struct node *temp,*ptr=head;
    temp=(struct node*)malloc(sizeof(struct node));
    printf("enter the data: ");
    scanf("%d",&temp->data);
    temp->next=NULL;
    while(ptr->next!=NULL){
        ptr=ptr->next;
    }
    ptr->next=temp;
    //free(ptr);
}
void insertbeginning(){
    struct node *a;
    a=(struct node*)malloc(sizeof(struct node));
    int data1;
    a->next=NULL;
    printf("enter the data: ");
    scanf("%d",&a->data);
    //a->data=data1;
    a->next=head;
    head=a;
}
int main(){
    int option;

    while(1){
        printf("1.createlist\n");
        printf("2.display\n");
        printf("3.insert\n");
        printf("4.delete\n");
        printf("5.insertend\n");
        printf("6.insertbegin\n");
        printf("7.reverse\n");
        printf("8.exit\n");
        printf("9.deletemid\n");
        printf("enter your option: ");

        scanf("%d",&option);

        switch(option){
            case 1:
                createlist();
                break;
            case 2:
                display();
                break;
            case 3:
                insert();
                break;
            case 4:
                del();
                break;
            case 5:
                insertend();
                break;
            case 6:
                insertbeginning();
                break;
            case 7:
                reverse();
                break;
            case 8:
                exit(5);
            case 9:
                deletemid();
                break;
        }
    }
}


void reverse(){
    struct node *current=head;
    struct node *prev=NULL;
    struct node *nxt=NULL;

    while(current!=NULL){
        nxt=current->next;
        current->next=prev;
        prev=current;
        current=nxt;
    }
    head=prev;
}

void deletemid(){ 
    struct node *temp,*ptr,*dup;
    ptr=(struct node*)malloc(sizeof(struct node));
    temp=(struct node*)malloc(sizeof(struct node));
    dup=(struct node*)malloc(sizeof(struct node));
    ptr=head;
    int c=0,k,i;

    while(ptr!=NULL){
        c+=1;
        ptr=ptr->next;
    }
    k=c/2;
    //printf("%d",k);
    ptr=head;
    if(ptr->next!=NULL){
    for(i=1;i<k;i++){
    
        ptr=ptr->next;
//c--;
    }
    dup=ptr;
    ptr->next=ptr->next->next;
    //free(dup);
    }

}
