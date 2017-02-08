from random import randint
class RandomizedSet(object):

    global ds
    global linked_ds
    global count
    def __init__(self):
        self.ds = {}
        self.count = 0
        self.linked_ds = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = True
        if self.ds.has_key(val):
            ret = False
        else:
            self.count += 1
            self.linked_ds[self.count] = val
            self.ds[val] = self.count 
        return ret

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        ret = False
        if self.ds.has_key(val):
            print self.linked_ds
            print self.ds
            ret = True
            key = self.ds[val]
            del self.ds[val]
            if key < self.count:
                tmp = self.linked_ds[self.count]
                self.linked_ds[key] = self.linked_ds[self.count]
                self.ds[tmp] = key
            del self.linked_ds[self.count]
            self.count -= 1
        print self.linked_ds    
        return ret    

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.count == 0:
            return None
        if self.count == 1:
            i = 1
        else:        
            i = randint(1, self.count)
        # print self.linked_ds
        # print i
        return self.linked_ds[i]
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print obj.insert(1)
print obj.insert(2)
print obj.remove(1)
print obj.insert(3)
print obj.remove(2)
print obj.getRandom()