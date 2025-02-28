import linkedlist as ll
import sys

longest_word = 36

debug = True


def main():
    if len(sys.argv) < 3:
        raise Exception("Usage: ./bard <INPUT FILE> <OUTPUT FILE>")

    shake = open("shakespeare-cleaned5.txt", "r")

    word = ""

    arr = [ll.LinkedList() for _ in range(longest_word + 1)]

    while True:
        word = shake.readline().rstrip()
   

        if not word:
            break
        length = len(word)

        if debug:
            if length > 36 or length < 0:
                print(length)

        arr[length].node_increment(word)

    shake.close()
    
    for i in range(5, longest_word + 1):
        arr[i].ll_sort()

    input = open(sys.argv[1], "r")
    output = open(sys.argv[2], "w")

    leng = freq = 0

    while True:
        line = input.readline()
        if not line:
            break
        line = line.rstrip().split(" ")

        # if debug:
        #     print(line)

        leng = int(line[0])
        freq = int(line[1])

        if leng > 36 or leng < 5 or not arr[leng].ll_get_head():
            output.write("-\n")
            continue

        curr = arr[leng].ll_get_head()
     
        # if debug:
        #     print(arr[leng].ll_print())

        i = 0
        while curr and i < freq:
            curr = curr.next
            i += 1

        if curr:
            output.write(curr.name + "\n")

        else:
            output.write("-\n")

    input.close()
    output.close()
    
if __name__ == "__main__":
    main()
