class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 10
        self.data = [-1] * 10

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        try:
            if(key > len(self.data)):
                newData = self.data
                self.data = [-1] * ( key * 2 )
                self.len = len(self.data)
                for i in range(len(newData)):
                    self.data[i] = newData[i]
                self.data[key] = value
            else:
                self.data[key] = value
        except IndexError:
            print(key,value)
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        try:
            return self.data[key]
        except IndexError:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        try:
            self.data[key] = -1
        except IndexError:
            print("No such index")

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
