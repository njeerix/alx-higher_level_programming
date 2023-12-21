#!/usr/bin/python3

"""
This module defines a Square class with a private size attribute.
"""


class Node:
    """Class Node that defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """
        Instatiation with data and next_node.

        Args:
            data (init): Data of the node (must be an integer).
            next_node (Node): Next node in the linked list (default is None).
                Must ne a Node object, otherwise raise a TypeError exception.

        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Seeter method to set the data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self,value):
        """Setter method to set the next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList that defines a singly linked list."""

    def __init__(self):
        """Simple instantiation."""
        self.head = None
    def sorted_insert(self, value):
        """
        Public instance method to insert a new Node into the correct sorted position in the list (increasing order).

        Args:
           value (int): Value to be inserted into the linked list.

        Returns:
            None
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Printable representation of the entire list.

        Returns:
            str: The entire list, one node number by line.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

