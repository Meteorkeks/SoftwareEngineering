from Iterator.DictClass import *
from Iterator.aIterator import *

lis = ListedArray()

lis.insertFirst("1")
lis.insertFirst("2")
lis.insertFirst("3")
lis.insertFirst("4")

it = ListedArrayIterator(lis)

print(it.currentItem().getValue())
print(it.next().getValue())



