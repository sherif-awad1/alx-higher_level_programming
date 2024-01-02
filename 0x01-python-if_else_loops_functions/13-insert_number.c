/*
 * File: insert_number
 *
 * Author: Sherif Awad
 */

#include "lists.h"

/**
 * insert_node - inserts num to singl list.
 * @head: pointer ot head
 * @number: number
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (n == NULL || n->n >= number)
	{
		new->next = n;
		*head = new;
		return (new);
	}

	while (n && n->next && n->next->n < number)
		n = n->next;
	new->next = n->next;
	n->next = new;

	return (new);
}
