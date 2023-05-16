#!/usr/bin/python3
"""class inherits and is a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """cache system has no limitations"""
    def __init__(self):
        """initializes the class attribute self"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """adds a new key-value pair to the cache"""
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                del self.cache_data[self.keys[0]]
                print("DISCARD: {}".format(self.keys[0]))
                self.keys.pop(0)
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets a value from the cache"""
        return self.cache_data.get(key)
