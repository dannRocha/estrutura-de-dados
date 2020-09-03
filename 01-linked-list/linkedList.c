#include <stdio.h>
#include <stdlib.h>

struct node {
  int value;
  struct node *next;
};

struct linked {
  struct node *head;
  struct node *tail;	
};


void unshift(struct linked *list, int value ){
  struct node *node = (struct node*) malloc(sizeof(struct node));
  node->value = value;
  node->next = list->head;
  list->head = node;
}



void echo(struct linked list){
  struct node *head = list.head;

  while(head != NULL){
  	printf("%d\n", head->value);
  	head = head->next;
  }
}

struct node delete(struct linked *list){
  struct node *node = list->head;
  list->head = list->head->next;
  return *node;
}

int main(){

  struct linked list;
  list.head = NULL;
  list.tail = NULL;

  unshift(&list, 10);
  unshift(&list, 11);
  unshift(&list, 12);

  
  echo(list);
    
  return 0;
}
