#!/usr/bin/env python
from collections import defaultdict


def read_input():
    with open("./inputs/day14") as f:
        template = [s for s in f.readline().strip()]
        lines = f.readlines()[1:]
    rules = {}
    for line in lines:
        pair, insert = line.strip().split(" -> ")
        rules[pair] = insert
    return template, rules


class ListNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return self.pair

    @property
    def pair(self):
        if self.next is None:
            return
        return f"{self.data}{self.next.data}"


def insert(node, el):
    new_node = ListNode(data=el)
    new_node.next = node.next
    node.next = new_node


def part1():
    template, rules = read_input()
    next_node = None
    for data in reversed(template):
        node = ListNode(data, next_node)
        next_node = node

    head = node = next_node
    for step in range(10):
        while node.next is not None:
            next_node = node.next
            insert(node, rules[node.pair])
            node = next_node
        node = head

    counter = defaultdict(int)
    while node.next is not None:
        counter[node.data] += 1
        node = node.next
    counter[node.data] += 1
    most = counter[max(counter, key=counter.get)]
    least = counter[min(counter, key=counter.get)]

    print(f"part 1: {most - least}")


if __name__ == "__main__":
    part1()
