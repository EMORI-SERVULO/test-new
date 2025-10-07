# Instructions
- Clone the repository
- Create a branch called `technical-challenge` were you will be adding all your work.
- Update readme with an `Execution Instructions` section explaining how to run/test you implementation.

# Challenge
### Doubly Linked lists

A doubly linked list is a data structure consisting of nodes, where each node contains data, a reference to the next node in the sequence, and a reference to the previous node.

**Example:**
```
      head
       |
       v
+------+------+     +------+------+     +------+------+     +------+------+     +------+------+
| prev | data |     | prev | data |     | prev | data |     | prev | data |     | prev | data |
|  -   |  10  | <---|  10  |  20  | <---|  20  |  20  | <---|  20  |  20  | <---|  20  |  30  |  <- tail
| next |      |--->| next |      |--->| next |      |--->| next |      |--->| next |      |
|  20  |      |     |  20  |      |     |  20  |      |     |  30  |      |     |  -   |      |
+------+------+     +------+------+     +------+------+     +------+------+     +------+------+
                                               ^                                       ^
                                               |--------------- DUPLICATES ------------|
```

Your task is to implement a doubly linked list from scratch, supporting the following operations:
- Insert head
- Insert tail
- Remove an element (By index or value, your choice)
- Remove all duplicate nodes of the given value, retaining only the first occurrence
- Search for an element, returning it's index if found
- Size of the list

Make sure to include an example testing your implementation.

# Additional details
- You can resolve the challenge using the programming language of your preference.

- You have 1 hour to complete the challenge.

- After finishing, upload the changes in a Pull Request, assign it to yourself and request review from Lorenzo Zuluaga ([L-Zuluaga](https://github.com/L-Zuluaga)).


**Good luck :)**
