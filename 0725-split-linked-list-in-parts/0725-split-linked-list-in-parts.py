class Solution(object):
    def splitListToParts(self, head, k):
        n = 0
        temp = head

        while temp:
            n += 1
            temp = temp.next


        base = n // k
        extra = n % k

        result = []
        current = head

        for i in range(k):

            size = base

            if i < extra:
                size += 1

            part_head = current

  
            for j in range(size - 1):
                if current:
                    current = current.next

     
            if current:
                next_part = current.next
                current.next = None
                current = next_part
                
            result.append(part_head)

        return result