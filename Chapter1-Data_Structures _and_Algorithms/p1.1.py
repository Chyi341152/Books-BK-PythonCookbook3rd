#!/usr/bin/python3
from collections import deque # list-like container with fast appends and pops on either end
import heapq  # Heap queue algorithm

# Unpacking a Sequence into Separate Variables
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

# Unpacking Elements from Iterables of Arbitrary Length
#   Solution: "star expressions"
def drop_first_last(grades):
    first, *middle, last = grades
    return middle
record = ('First Name', 'xyz@gmail.com','abc@gmail.com', 'Last Name')
middle = drop_first_last(record)
print(middle)

#
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)

# Keeping the Last N Items
def search(lines, pattern, history=2):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('sample.txt') as f:
        for line, previous in search(f, 'python', 2):
            for pline in previous:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
    
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    # Adding or popping items from either end of a queue has O(1) complexity
    q.appendleft(4)
    print(q)
    print(q.pop())
    
    # Finding the Largest or Smallest N Items
    # heapq module has two functions - nlargest() and nsmallest()
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))
    
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print('cheap: {}'.format(heapq.nsmallest(3, portfolio, key=lambda s: s['price'])))
    print('expensive: {}'.format(heapq.nlargest(3, portfolio, key=lambda s: s['price'])))
    
    nums = [1,8,2,23,7,-4,18,23,42,37,2]
    import heapq
    heap = list(nums)
    heapq.heapify(heap) # Transform list x into a heap, heap[0] is always the smallest item
    print(heap)
    print(heap[0])
    print(heapq.heappop(heap))

    