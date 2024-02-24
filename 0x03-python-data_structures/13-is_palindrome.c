#include "lists.h"

/**
 * is_palindrome - function checks if list is palindrome by calling check_pal
 * @head: pointer to the beginning of the list
 * Return: if not palindrome return 0 else 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}

/**
 * check_pal - function checking if list is palindrome
 * @head: pointer to the list's beginning
 * @last: pointer to the list's end
 * Return: if not palindrom return 0 else 1
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
