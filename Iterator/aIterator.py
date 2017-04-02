

from abc import ABCMeta, abstractmethod
from Iterator.DictClass import *

class aIterator(metaclass=ABCMeta):

    @abstractmethod
    def __iter__(self, liste):
        return self

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def islast(self):
        pass

    @abstractmethod
    def currentItem(self):
        pass

class DictClassIterator(aIterator):

    count = None
    dic = None

    def __iter__(self, dicclass):
        self.dic = dicclass
        return self

    def next(self):
        pass

    def first(self):
        pass

    def islast(self):
        pass

    def currentItem(self):
        pass

class ListedArrayIterator(aIterator):
    _list = None
    _ele_tmp = None

    def __iter__(self, listclass: ListedArray):
        self._list = listclass
        self._ele_tmp = listclass.firstElement  # type: ListedArrayElement
        return self

    def next(self):
        return self._ele_tmp.nextElement  # type: ListedArrayElement

    def first(self):
        return self._list.firstElement  # type: ListedArrayElement

    def islast(self):
        return self._ele_tmp is self._list.lastElement  # type: bool

    def currentItem(self):
        return self._ele_tmp  # type: ListedArrayElement