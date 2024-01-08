#include "lists.h"
/**
 * is_palindrome - checks if list is palindrome
 * @head: address of head node
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int len, *arr, i;
	listint_t *ptr = *head;

	if (!head || !(*head) || !((*head)->next))
		return (1);
	len = 0;
	while (ptr)
	{
		len += 1;
		ptr = ptr->next;
	}
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);
	ptr = *head;
	for (i = 0; i < len; i++)
	{
		arr[i] = ptr->n;
		ptr = ptr->next;
	}
	array_rev(arr, len);
	ptr = *head;
	for (i = 0; i < len; i++)
	{
		if (ptr->n != arr[i])
		{
			free(arr);
			return (0);
		}
		ptr = ptr->next;
	}
	free(arr);
	return (1);
}

/**
 * array_rev - reverses array
 * @arr: array to reverse
 * @len:length of array to reverse
 *
 * Retrun: no return value
 */
void array_rev(int *arr, int len)
{
	int i, tmp;

	for (i = 0; i < (len / 2); i++)
	{
		tmp = arr[i];
		arr[i] = arr[(len - 1) - i];
		arr[(len - 1) - i] = tmp;
	}
}


