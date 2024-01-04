#include "lists.h"
/**
 * check_cycle - checks if list is a cycle
 * @list: head of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (!list)
		return (0);
	current = list;
	while (current->next != NULL)
	{
		if (current->next == list)
			return (1);
		else
			current = current->next;
	}
	return (0);
}
