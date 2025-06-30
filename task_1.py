class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # За завданням обрав сортування списку методом вставок
    def insertion_sort(self):
        sorted_list = None  
        current = self.head

        while current:
            next_node = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next

                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_list

    @staticmethod
    def merge_sorted_lists(list1: "LinkedList", list2: "LinkedList") -> "LinkedList":
        merged_list = LinkedList()
        node = Node() 
        tail = node

        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.data <= current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2

        merged_list.head = node.next
        return merged_list


# Приклад використання
llist = LinkedList()

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

llist.reverse_linked_list()
print("\nЗв'язний список після реверсування:")
llist.print_list()

llist.insertion_sort()
print("\nВідсортований зв'язний список ( метод вставок ):")
llist.print_list()


llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)


merged_list = LinkedList.merge_sorted_lists(llist1, llist2)
print("\nОб'єднані два відсортовані однозв'язні списки в один відсортований список:")
merged_list.print_list()
