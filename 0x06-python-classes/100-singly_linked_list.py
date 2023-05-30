#!/usr/bin/python3
"""Node Module"""


class Node:
    """defines a class node of a singly linked list"""

    def __init__(self, data, next_node=None) -> None:
        """
        Instatiates class nod attributes

        Attributes:
            data: node value
            next_node: next node address
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets linked list data"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Gets linked list next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self) -> None:
        """Instantiates private atttribute"""
        self.__head = None

    def __init__(self) -> str:
        """prints string in a SinglyLinkedList"""
        outp = list()
        fut = self.__head

        while fut is not None:
            outp.append(str(fut.data))
            fut = fut.next_Node

        return "\n".join(outp)

    def sorted_insert(self, value):
        """
        sort the value of the node

        Attributes:
            value: node value
        """

        if self.__head is None:
            self.__head = Node(value)
            return

        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return

        fut, initial = self.__head.next_node, self.__head
        while fut is not None:
            if value < fut.data:
                initial.next_node = Node(value, future)
                return
            initial = fut
            fut = fut.next_node
        initial.next_node = Node(value)
