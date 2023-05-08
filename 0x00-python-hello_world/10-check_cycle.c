#include "lists.h"

/**
  * check_cycle - A function checking cycle in a stringly linked
  * @list: where the cycle is checked
  * Return: 1 on success, otherwise 0
  */

int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list && list->next)
	{
		tmp = list->next;
	}
	else
	{
		return (0);
	}
	while (list && tmp)
	{
		if (list == tmp)
		{
			return (1);
		}
		list = list->next;

		if (tmp->next)
		{
			tmp = tmp->next;
		}
		else
		{
			return (0);
		}

		if (tmp->next)
			tmp = tmp->next;
		else
			return (0);
	}
	return (0);
}
