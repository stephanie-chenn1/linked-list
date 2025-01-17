
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head is None:
            return None
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n); worst case would be the last element of our list to match our val
    # Space Complexity: O(1)
    def search(self, value):
        if self.head is None:
            return False
        
        current = self.head
        while current is not None:
            if current.value != value:
                current = current.next
            else:
                return True
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n); need to traverse through entire list to get count
    # Space Complexity: O(1)
    def length(self):
        if self.head is None:
            return 0
        
        length = 0
        current = self.head

        while current is not None:
            current = current.next
            length += 1
        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if index < 0:
            return None
        
        current_index = 0
        current = self.head

        if current is None:
            return None

        while current is not None and current_index < index:
            current = current.next
            current_index += 1
        return current.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head is None:
            return None

        current = self.head

        while current is not None:
            if current.next:
                current = current.next
            else:
                return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
        else:
            current = self.head

            while current is not None:
                if current.next:
                    current = current.next
                else:
                    new_node = Node(value)
                    current.next = new_node
                    current = current.next
                    break


    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        if self.head is None:
            return None
        
        current_max = self.head.value
        current = self.head

        while current is not None:
            if current_max < current.value:
                current_max = current.value
            current = current.next
        return current_max

    # method to delete the first node found with specified value
    # Time Complexity: O(n); our worst case is that we need to traverse through the entire list to remove last element
    # Space Complexity: O(1)
    def delete(self, value):
        if self.head is None:
            return None

        current = self.head
        previous = self.head

        while current is not None:
            if current.value != value:
                previous = current
                current = current.next
            else:
                if self.head.value == value: # when we remove first element
                    self.head = current.next
                    current = current.next
                elif not current.next: # when we remove last element
                    current = None
                    previous.next = None
                else: # when we remove a middle element
                    current = current.next
                    previous.next = current

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n); creating a new data struture to hold all values 
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        # iterative method
        if self.head is None:
            return None

        current = self.head
        previous = None

        while current is not None:
            saved_next = current.next
            current.next = previous
            previous = current
            current = saved_next
        self.head = previous

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        length = 0
        current = self.head

        while current is not None:
            length += 1
            current = current.next
        
        mid = length //2
        current = self.head
        idx = 0

        while idx < mid:
            idx += 1
            current = current.next
        return current.value

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        if self.head is None:
            return None
        
        length = 0
        current = self.head

        # gets total length of array
        while current is not None:
            length += 1
            current = current.next
        
        current = self.head

        if n > length:
            return None
        idx = length-1 # starting index from beginning of linked list with be length-1 in terms of nth node from end
        while current is not None:
            if idx != n:
                idx -= 1
            else:
                return current.value
            current = current.next

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        s = set()
        current = self.head

        while current is not None:
            if current in s:
                return True
            s.add(current)
            current = current.next
        return False
            

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
