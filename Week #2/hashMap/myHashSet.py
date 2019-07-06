class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [-1] * 10

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        try:
            if(key > len(self.data)):
                newData = self.data
                self.data = [-1] * (key * 2)
                for i in range(len(newData)):
                    self.data[i] = newData[i]
                self.data[key] = 1
            else:
                self.data[key] = 1
        except IndexError:
            print(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        try:
            self.data[key] = -1
        except IndexError:
            print(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        try:
            if(self.data[key] == 1):
                return True
            else:
                return False
        except IndexError:
            print(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
