#include "lists.h"

void printLinkedList(SinglyLinkedListNode *head)
{
	SinglyLinkedListNode *current = head;

	while (current)
	{
		printf("%d\n", current->data);
		current = current->next;
	}
}

int main(void)
{
	SinglyLinkedListNode *head, *new;

	head = (SinglyLinkedListNode *)malloc(sizeof(SinglyLinkedListNode));
	new = (SinglyLinkedListNode *)malloc(sizeof(SinglyLinkedListNode));

	head->data = 1;
	head->next = NULL;

	new->data = 2;
	new->next = NULL;

	head->next = new;

	printLinkedList(head);

	return (0);
}
