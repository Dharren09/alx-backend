#!/usr/bin/python3
"""creates a class that inherits and is a caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """least recently used cache"""
    """initializes the class instance"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """adds a new key value pair to the caching system"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """gets the value from the caching system"""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
