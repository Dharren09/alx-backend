#!/usr/bin/python3
""" creating a class that inherits another class
and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system has no limit"""
    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the
        item value for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get the vakue in self.cache_data linked to the key"""
        return self.cache_data.get(key)
