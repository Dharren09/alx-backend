#!/usr/bin/env python3
"""creates a class that inherits and is a caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """caching system is unlimited"""
    def __init__(self):
        """initializes the self attributte of the class"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """adds a new key value pair to the cache"""
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                last = self.keys.pop()
                print("DISCARD: {}".format(last))
                del self.cache_data[last]
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """gets the value from the caching system"""
        return self.cache_data.get(key)
