import inspect

class DictClass:
    _dic = {}

    def __init__(self, dic):
        self._dic = dic

    def set(self, key,  value):
        self._dic[key] = value

class ListedArrayElement():
    nextElement = None
    prevElement = None
    _value = None

    def __init__(self, prev=None, next=None):
        self.nextElement = next
        self.prevElement = prev

    def setPrevElement(self, ele):
        self.prevElement = ele

    def setNextElement(self, ele):
        self.nextElement = ele

    def setValue(self, value):
        self._value = value

    def getValue(self):
        return self._value



class ListedArray():
    firstElement = None
    lastElement = None

    def insertBefore(self, ele1: ListedArrayElement, ele2: ListedArrayElement):
        if not isinstance(ele2, ListedArrayElement):
            ele3 = ListedArrayElement()
            ele3.setValue(ele2)
            ele2 = ele3
        ele_tmp = self.firstElement
        while ele_tmp is not ele1:
            ele_tmp = ele_tmp.nextElement

        ele_tmp.prevElement = ele2
        ele2.prevElement = ele_tmp.prevElement
        ele2.nextElement = ele_tmp
        ele_tmp.prevElement = ele2

    def insertAfter(self, ele1: ListedArrayElement, ele2: ListedArrayElement):
        if not isinstance(ele2, ListedArrayElement):
            ele3 = ListedArrayElement()
            ele3.setValue(ele2)
            ele2 = ele3
        ele_tmp = self.firstElement
        while ele_tmp is not ele1:
            ele_tmp = ele_tmp.nextElement

        ele2.prevElement = ele_tmp
        ele2.nextElement = ele_tmp.nextElement
        ele_tmp.nextElement.prevElement = ele2
        ele_tmp.nextElement = ele2

    def insertFirst(self, ele):
        if self.firstElement is not None:
            self.insertBefore(self.firstElement, ele)
        else:
            self.lastElement = ele
        self.firstElement = ele

    def insertLast(self, ele):
        if self.firstElement is not None:
            self.insertAfter(self.lastElement, ele)
        else:
            self.firstElement = ele
            self.lastElement = ele

