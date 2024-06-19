#ifndef Lists_H
#define Lists_H
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct SinglyLinkedListNode SinglyLinkedListNode;
typedef struct SinglyLinkedList SinglyLinkedList;

struct SinglyLinkedListNode
{
    int data;
    SinglyLinkedListNode *next;
};

struct SinglyLinkedList
{
    SinglyLinkedListNode *head;
    SinglyLinkedListNode *tail;
};

void printLinkedList(SinglyLinkedListNode *head);
#endif
