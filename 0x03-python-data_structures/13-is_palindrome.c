#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome by calling check_pall
 * @head: pointer to beginning of list
 * Return: if not palindrome return 0 else 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}

/**
 * check_pal - checks if list is palindrome
 * @head: beginning of list ptr
 * @last: end of list ptr
 * Return: if not palindrome return 0 else 1
 */
int check_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
