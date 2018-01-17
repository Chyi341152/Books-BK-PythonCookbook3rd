# Removing Duplicates from a Sequence while Maintaining Order
# You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items

def dedupe(items): # sequence are hashable
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

# def dedupe(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
#
# a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))

# set doesn't preserve any kind of ordering

with open('sample.txt','r') as f:
    for line in dedupe(f):
        print(line)