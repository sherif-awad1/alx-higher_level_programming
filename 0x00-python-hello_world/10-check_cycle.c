/*
 * File: check_cycle
 *
 * Author: sherif awad
 */
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks singl list have cycle
 * @list:list
 * Return: 0 on success
 */
int check_cycle(listint_t *list)
{
	listint_t *l, *c;

	if (list == NULL || list->next == NULL)
		return (0);
	l = list->next;
	c = list->next->next;
	while (l && c && c->next)
	{
		if (l == c)
			return (1);
		l = l->next;
		c = c->next->next;
	}
	return (0);
}
