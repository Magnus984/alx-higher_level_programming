#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts number into a
 * sorted singly linked list
 * @head: address of head node
 * @number: number to insert into list
 *
 * Return: address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *temp;
	int nxt_val, value;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (current == NULL || number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next != NULL)
	{
		value = current->n;
		nxt_val = current->next->n;
		if (number >= value && number <= nxt_val)
		{
			temp = current->next;
			current->next = new;
			new->next = temp;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	return (new);
}
