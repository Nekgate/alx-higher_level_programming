#include "lists.h"

/**
 * is_palindrome - check for palindrome linkedlist
 * @head: linkedlist
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *cp = *head;
	int buff[10240], initz = 0, end = 0;

	if (!*head || !((*head)->next))
		return (1);

	while (cp)
	{
		buff[end] = cp->n;
		cp = cp->next;
		end++;
	}

	end--;

	while (initz <= end / 2)
	{
		if (buff[initz] != buff[end - initz])
			return (0);
		initz++;
	}

	return (1);
}
