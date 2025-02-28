class Node:

    def __init__(self):
        self.freq = 0
        self.name = ""
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def node_increment(self, key):
        curr = self.head
        while curr:
            if curr.name == key:
                curr.freq += 1
                return

            curr = curr.next

        self.ll_insert(key)

    def ll_insert(self, word):
        add = Node()
        add.name = word
        add.next = self.head
        self.head = add
        return

    def ll_length(self):
        length = 0
        curr = self.head

        while curr:
            length += 1
            curr = curr.next

        return length

    def swap(self, first, second):

        first.freq, second.freq = second.freq, first.freq
        first.name, second.name = second.name, first.name

    def ll_sort(self):
        for i in range(self.ll_length() - 2, -1, -1):
            curr = self.head
            temp = curr.next

            for _ in range(i + 1):

                # swap the nodes if the curr frequency is less than the temp frequncy
                # or if the frequencies are equal but the name of the curr node is
                # greater lexicographically than the name of the temp node
                if (curr.freq < temp.freq
                    or (curr.freq == temp.freq
                        and curr.name > temp.name)):
                    self.swap(curr, temp)
                    # curr, temp = temp, curr

                curr = temp
                temp = temp.next

        return

    def ll_get_head(self):
        return self.head

    def ll_print(self):
        list_str = ""
        curr = self.head

        while curr:
            list_str += curr.name + " " + str(curr.freq) + " "
            curr = curr.next

        return list_str.rstrip()
