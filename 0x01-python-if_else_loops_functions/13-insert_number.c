#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
  * insert_node - function that inserts node in a sorted list
  * @head: head of the node
  * @number: insert node value
  * Return: new node address if successful, otherwise NULL
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL, *current = NULL;

	current = *head;
	if (!(*head) || current->n >= number)
	{
		newNode = malloc(sizeof(listint_t));
		if (!newNode)
			return (NULL);
		newNode->n = number;
		newNode->next = current;
		*head = newNode;
		return (newNode);
	}
	while (current)
	{
		if (current->n <= number && (!current->next || current->next->n > number))
		{
			newNode = malloc(sizeof(listint_t));
			if (!newNode)
				return (NULL);
			newNode->n = number;
			newNode->next = current->next;
			current->next = newNode;
			return (newNode);
		}
		else
		{
			current = current->next;
		}
	}
	return (NULL);
}
