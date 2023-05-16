#!/usr/bin/python3
"""creates a class that inherits and is a caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """initializes the class"""
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """adds a new key value pair to the caching system"""
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(0)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """gets the value from the caching system"""
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
