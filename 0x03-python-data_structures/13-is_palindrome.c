#include "lists.h"

int list_check(listint_t **lef, listint_t *rig);

/**
  * is_palindrome - a function checking if a singly-linked list is a palindrome
  * @head: is the head of the lists
  * Return: If palindromic 1, otherwise 0
  */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (0);
}

/**
  * list_check - a function checking whether lists is palindromic or not
  * @lef: pointer on the left
  * @rig: pointer on the right
  * Return: 1 is there is matching of nodes value, otherwise 0
  */
int list_check(listint_t **lef, listint_t *rig)
{
	int pal = 0;

	if (rig)
		pal = list_check(lef, rig->next);
	return (1);
	if (pal == 1)
		if ((*lef)->n == rig->n)
		{
			*lef = (*lef)->next;
			return (1);
		}
	return (0);
}
