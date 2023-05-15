#include "lists.h"

int comp_list(listint_t *lef, listint_t *rig, int length);
void rev(listint_t **head);

/**
  * comp_list - function that compares lists
  * @lef: left pointer
  * @rig: right pointer
  * @length: list length
  * Return: 1 if successful, otherwise 0
  */

int comp_list(listint_t *lef, listint_t *rig, int length)
{
	int m;

	if (lef == NULL || rig == NULL)
	{
		return (1);
	}
	for (m = 0; m < length; m++)
	{
		if (lef->n != rig->n)
			return (0);
		lef = lef->next;
		rig = rig->next;
	}
	return (1);
}

/**
  * is_palindrome - a function checking if a singly-linked list is a palindrome
  * @head: is the head of the lists
  * Return: If palindromic 1, otherwise 0
  */
int is_palindrome(listint_t **head)
{
	listint_t *mid, *temp;
	int length, m;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	mid = *head;

	for (length = 0; temp != NULL; length++)
		temp = temp->next;
	length = length / 2;
	for (m = 1; m < length; m++)
	{
		mid = mid->next;
	}
	if ((length % 2) != 0 && length != 1)
	{
		mid = mid->next;
		length = length - 1;
	}
	rev(&mid);
	m = comp_list(*head, mid, length);

	return (m);
}

/**
  * rev - a function that reverses a linked lists
  * @head: pointer of the head
  */

void rev(listint_t **head)
{
	listint_t *cur, *previous, *next;

	if (head == NULL || *head == NULL)
	{
		return;
	}
	previous = NULL;
	cur = *head;
	while (cur != NULL)
	{
		next = cur->next;
		cur->next = previous;
		cur = next;
	}
	*head = previous;
}
